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
    anchor_dict = {"Create Buyer":"/createbuyer", "Create Deal":"/createdeal", "Map":"/map", "Logout":"/logout"}
    return render_template('profile.html', current_user=current_user, anchor_dict=anchor_dict)


@app.route("/map", methods=['GET'])
@login_required
def map():
    return render_template('map.html')


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

            flash(f"Buyer with id '{buyer.id}' created", 'success')
            return redirect(url_for('profile'))

        except sqlalchemy.exc.IntegrityError:
            flash("ERROR: A buyer with this id or CNIC already exists!")
            return render_template('createbuyer.html', form=form)         
            
    return render_template('createbuyer.html',  form=form)

@app.route("/createdeal", methods=['GET', 'POST'])
@login_required
def createdeal():

    form = CreateDealForm()
    if form.validate_on_submit():
        #Quering the mentioned plot and buyer returns None is no such pot exists        
        plot = Plot.query.filter_by(id=form.plot_id.data).first()
        buyer = Buyer.query.filter_by(id=form.buyer_id.data).first()

        ##Applying validity checks
        if plot is None:       
            flash(f"No plot exists with Plot ID: {form.plot_id.data}")
            return render_template('createdeal.html', form=form)

        if buyer is None:
            flash(f"No buyer exists with Buyer ID: {form.buyer_id.data}")
            return render_template('createdeal.html', form=form)

        if plot.deal is not None:        
            flash(f"The Plot with ID {plot.id} cannot be sold")
            flash(f"Plot Status: {plot.status}")
            flash(f"Plot's Deal ID: {plot.deal.id}")
            return render_template('createdeal.html', form=form)


        ##UPDATING CORESPONDING PLOT STATUS
        plot.status = 'sold' if form.first_amount_recieved.data == plot.price else 'in a deal'
        #db.session.commit()

        try:
            #Creating Deal object
            deal = Deal(
                id                      = form.id.data,
                buyer_id                = form.buyer_id.data,
                plot_id                 = form.plot_id.data,
                signing_date            = datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                status                  = 'finished' if form.first_amount_recieved.data == plot.price else 'on going',
                amount_per_installment  = form.amount_per_installment.data,
                installment_frequency   = form.installment_frequency.data,
                comments                = form.comments.data if form.comments.data else db.null()
            )

            db.session.add(deal)
            #db.session.commit()

        except sqlalchemy.exc.IntegrityError:
            flash("ERROR: A deal with this ID already exists!")
            return render_template('createdeal.html', form=form)

        
        #Creating corresponding transaction
        transaction = Transaction(
            amount = form.first_amount_recieved.data,
            date_time = datetime.now(),  
            comments = f"Initial Transaction for Deal {form.id.data}",
            deal_id = form.id.data
        )

        db.session.add(transaction)
        db.session.commit()
        flash(f"Deal with ID {deal.id} successfully created!")
        return redirect(url_for('profile'))

    return render_template('createdeal.html', form=form)


@app.route("/logout", methods=['GET'])
@login_required
def logout():
    logout_user()
    flash('User logged out', 'info')
    return redirect(url_for('home'))