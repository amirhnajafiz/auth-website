from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)  # Creating a blueprint instance



# Create a view or blueprint
@views.route('/')
@login_required  # User can only access the home page if it is logged in
def home():  # Creating the home end-point
    return render_template("home.html", user=current_user)  # Reference to current user in home page
