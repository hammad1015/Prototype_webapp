from flask import Blueprint, redirect, render_template, flash, request, session, url_for
from flask import current_app as app
from flask_login import login_required, logout_user, current_user, login_user
from flask_sqlalchemy import sqlalchemy

from .forms import LoginForm, CreateBuyerForm
from .model import db, User, Buyer
from . import login_manager


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
    return render_template('profile.html', current_user=current_user)


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


@app.route("/logout", methods=['GET'])
@login_required
def logout():
    logout_user()
    flash('User logged out', 'info')
    return redirect(url_for('home'))