from flask import Blueprint, redirect, render_template, flash, request, session, url_for
from flask import current_app as app
from flask_login import login_required, logout_user, current_user, login_user

from .forms import LoginForm
from .model import db, User
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
    #print("IN user_loader:", user_id, type(user_id))
    return User.query.get(int(user_id))
    #return None


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash('You must be logged in to view that page', 'danger')
    return redirect(url_for('login'))


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        #print("User is is authenticated")
        flash('You are already logged in', 'info')
        return redirect(url_for('profile'))  

    form = LoginForm()
    # Validate login attempt
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()  
        if user and user.check_password(password1=form.password.data):
            #print("********************88\n", user, "\n********************")
            #print(user)
            login_user(user)
            #next_page = request.args.get('next')
            flash(f'Welcome {user.username}', 'success')
            return redirect(url_for('profile'))

        flash('Invalid username/password combination', 'danger')
        return redirect(url_for('login'))  

    return render_template('loginpage.html', form=form)  



@app.route("/profile", methods=['GET', 'POST'])
@login_required
def profile():
    return render_template('profile.html', current_user=current_user)


@app.route("/logout", methods=['GET'])
@login_required
def logout():
    logout_user()
    flash('User logged out', 'info')
    return redirect(url_for('home'))