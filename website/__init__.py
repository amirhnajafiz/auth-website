from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


db = SQLAlchemy()  # Creating an instanse of SQLAlchemy object for database
DB_NAME = 'database.db'


def create_app():  # Creating an flask app and setting the secret key
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'iqbnddpoeallwennvcpwee'  # Secret key is for sessions hashing
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'  # Store the database into a SQLite file
    db.init_app(app)  # Set the app for database

    # Importing the blueprints
    from .views import views
    from .auth import auth

    # Registering the blueprints
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    # We just want to import the classes so we have them defined
    from .models import User, Note

    create_database(app)  # Creating the website database

    login_manager = LoginManager()  # Tells flask what to do if user is not logged in
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):  # This tells flask how to get a user
        return User.query.get(int(id))


    return app


def create_database(app):  # Check if database exists or not and then it creates it if it dosen't exist
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
