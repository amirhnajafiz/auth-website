from flask import Blueprint

auth = Blueprint('auth', __name__)  # Creating a blueprint instance


# Blueprints and endpoints of the application
@auth.route('/login')
def login():  # The login route
    return "<p>Login</p>"


@auth.route('/logout')
def logout():  # Logging out function
    return "<p>Logout</p>"


@auth.route('/sign-up')
def sign_up():  # Registering applications
    return "<p>Sign Up</p>"
