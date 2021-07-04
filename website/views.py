from flask import Blueprint

views = Blueprint('views', __name__)  # Creating a blueprint instance



# Create a view or blueprint
@views.route('/')
def home():  # Creating the home end-point
    return "<h1>Test</h1>"
    