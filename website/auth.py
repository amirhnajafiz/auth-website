from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)  # Creating a blueprint instance


# Blueprints and endpoints of the application
@auth.route('/login', methods=['GET', 'POST'])
def login():  # The login route
    return render_template("login.html")


@auth.route('/logout')
def logout():  # Logging out function
    return "<p>Logout</p>"


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():  # Registering applications
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # Inputs validation
        if len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(firstname) < 2:
            flash('First name must be greater than 1 characters.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            flash('Account created!', category='success')

    return render_template("sign_up.html")
