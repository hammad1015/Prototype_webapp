from flask import Blueprint, redirect, render_template, flash, request, session, url_for
from flask import current_app as app
from flask_login import login_required, logout_user, current_user, login_user

from .forms import LoginForm
from .model import db, User
#from . import login_manager


@app.route("/", methods=['GET'])
@app.route("/home", methods=['GET'])
def home():
    return render_template('home.html')


@app.route("/about", methods=['GET'])
def about():
    return render_template('about.html')


#@login_manager.user_loader
#def load_user(user_id):
#    return User.get_id(user_id)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))  

    form = LoginForm()
    # Validate login attempt
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()  
        if user and user.check_password(password=form.password.data):
            #login_user(user)
            #next_page = request.args.get('next')
            return redirect(url_for('profile'))

        flash('Invalid username/password combination')
        return redirect(url_for('login'))  

    return render_teemplate('loginpage.html', form=form)  



@app.route("/profile", methods=['GET', 'POST'])
def profile():
    return render_template('profile.html')