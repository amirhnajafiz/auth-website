from flask import Flask

def create_app():  # Creating an flask app and setting the secret key
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'iqbnddpoeallwennvcpwee'  # Secret key is for sessions hashing

    # Importing the blueprints
    from .views import views
    from .auth import auth

    # Registering the blueprints
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app