from flask import Blueprint, render_template

views = Blueprint('views', __name__)  # Creating a blueprint instance



# Create a view or blueprint
@views.route('/')
def home():  # Creating the home end-point
    return render_template("home.html")
