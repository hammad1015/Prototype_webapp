from flask import Blueprint, redirect, render_template, flash, request, session, url_for
from flask import current_app as app
from flask_login import login_required, logout_user, current_user, login_user
from flask_sqlalchemy import sqlalchemy

from .forms import LoginForm, CreateBuyerForm, CreateDealForm
from .model import db, User, Buyer, Deal, Plot, Transaction
from . import login_manager

from datetime import datetime


@app.route("/", methods=['GET'])
@app.route("/home", methods=['GET'])
def home():
    return render_template('home.html')


@app.route("/about", methods=['GET'])
def about():
    return render_template('about.html')


#This function should return the user for the user_id
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash('You must be logged in to view that page', 'danger')
    return redirect(url_for('login'))


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('You are already logged in', 'info')
        return redirect(url_for('profile'))  

    form = LoginForm()
    # Validate login attempt
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and user.check_password(password1=form.password.data):
            login_user(user)
            flash(f'Welcome {user.username}', 'success')
            return redirect(url_for('profile'))

        flash('Invalid username/password combination', 'danger')
        return redirect(url_for('login'))  

    return render_template('loginpage.html', form=form)


@app.route("/profile", methods=['GET', 'POST'])
@login_required
def profile():
    anchor_dict = {"Create Buyer":"/createbuyer", "Logout":"/logout"}
    return render_template('profile.html', current_user=current_user, anchor_dict=anchor_dict)


@app.route("/createbuyer", methods=['GET', 'POST'])
@login_required
def createbuyer():

    form = CreateBuyerForm()
    if form.validate_on_submit():        
        try:
            buyer = Buyer(
                id       = form.id.data,
                name     = form.name.data,
                cnic     = form.cnic.data,
                comments = form.comments.data if form.comments.data else db.null()
            )

            db.session.add(buyer)
            db.session.commit()

        except sqlalchemy.exc.IntegrityError:
            flash("ERROR: A buyer with this id or CNIC already exists!")
            return redirect(url_for('createbuyer'))        

        finally:
            flash(f"Buyer with id '{buyer.id}' created", 'success')
            return redirect(url_for('profile'))

    return render_template('createbuyer.html',  form=form)

@app.route("/createdeal", methods=['GET', 'POST'])
@login_required
def createdeal():

    form = CreateDealForm()
    if form.validate_on_submit():
        #Quering the mentioned plot
        try:
            plot = Plot.query.filter_by(id=form.plot_id.data).first()
        except Exception:
            flash(f"No plot exists with Plot ID: {form.plot_id.data}")
            return redirect(url_for('createdeal'))
        finally:
            if plot.status.lower() == "sold":
                flash(f"The plot with Plot ID: {form.plot_id.data} is  already sold")
                return redirect(url_for('profile'))
            elif plot.status.lower() == "on going":
                flash(f"The plot with Plot ID: {form.plot_id.data} is  already a part of an on going deal with ID: {plot.deal.id}")
                return redirect(url_for('profile'))

        ##UPDATE CORESPONDING PLOT STATUS 

        try:
            #Creating Deal object
            deal = Deal(
                id = form.id.data,
                buyer_id = form.buyer_id.data,
                plot_id = form.plot_id.data,
                signing_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                status = 'sold' if form.first_amount_recieved.data == plot.price else 'on going',
                amount_per_installment = form.amount_per_installment.data,
                installment_frequency = form.installment_frequency.data,
                comments = form.comments.data if form.comments.data else db.null()
            )

            db.session.add(deal)
            db.session.commit()

        except sqlalchemy.exc.IntegrityError:
            flash("ERROR: A deal with this ID already exists!")
            return redirect(url_for('createdeal'))

        
        #Creating corresponding transaction
        transaction = Transaction(
            amount = form.first_amount_recieved.data,
            date_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            comments = f"Initial Transaction for Deal {form.id.data}",
            deal_id = form.id.data
        )

        db.session.add(transaction)
        db.session.commit()


    return render_template('createdeal.html', form=form)


@app.route("/logout", methods=['GET'])
@login_required
def logout():
    logout_user()
    flash('User logged out', 'info')
    return redirect(url_for('home'))