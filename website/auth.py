"""auth file

The endpoints of Authorizing in our website is being handle here.

This is the Auth blueprints.
Registeration and logging in, amoung of logging out.
Hashings and password validation also is handling here.
"""
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User 
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user



auth = Blueprint('auth', __name__)  # Creating a blueprint instance


# Blueprints and endpoints of the application
@auth.route('/login', methods=['GET', 'POST'])
def login():
    """The login route

    The login function gets the email and password and checks
    for user in database and then validates the information.

    It return error messages or redirects user to home page.
    """
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash(message='Logged in sucessfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash(message='Incorrect password, try again.', category='warning')
        else:
            flash(message='Email does not exists.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required  # Works if user is login
def logout(): 
    """Logging out function

    Removes the user from session and redirects to auth.login endpoint.
    """
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():   
    """Registering applications

    The endpoint of registration, where it gets the user data
    validates them, and if it was all done correctly, it addes a
    new user to database and redirects to Views.home page.
    """
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()

        # Inputs validation
        if user:  # Check for duplicate emails
            flash(message='Email already exists.', category='error')
        elif len(email) < 4:  # Email validation
            flash(message='Email must be greater than 4 characters.', category='error')
        elif len(firstname) < 2:  # First name limit
            flash(message='First name must be greater than 1 characters.', category='error')
        elif password1 != password2:  # Password confirm
            flash(message='Passwords don\'t match.', category='error')
        elif len(password1) < 7:  # Password limit
            flash(message='Password must be at least 7 characters.', category='error')
        else:  # Creating a new user
            newUser = User(email=email, first_name=firstname, password=generate_password_hash(password1, method='sha256'))
            db.session.add(newUser)  # Commit the new user to database
            db.session.commit()
            flash(message='Account created!', category='success')
            login_user(newUser, remember=True)
            return redirect(url_for('views.home'))  # Redirecting to home page

    return render_template("sign_up.html", user=current_user)
