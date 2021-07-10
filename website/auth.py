from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)  # Creating a blueprint instance


# Blueprints and endpoints of the application
@auth.route('/login')
def login():  # The login route
    return render_template("login.html")


@auth.route('/logout')
def logout():  # Logging out function
    return "<p>Logout</p>"


@auth.route('/sign-up')
def sign_up():  # Registering applications
    return render_template("sign_up.html")
