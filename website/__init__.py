from flask import Flask

def create_app():  # Creating an flask app and setting the secret key
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'iqbnddpoeallwennvcpwee'  # Secret key is for sessions hashing

    return app