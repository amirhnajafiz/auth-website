from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
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

    return app