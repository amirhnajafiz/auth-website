# Flasking

Implement a full website with Python Flask framework.

This is a course that I watched from youtube, about creating a website with python Flask framework.

## Tools we need to setup the project

First things first, install flask framework:
```shell
pip install flask
```

Flask-log in provides user session management for flask.
Check the github sourse in [here](https://github.com/maxcountryman/flask-login).
Install flask-login module:
```shell
pip install flask-login
```

Flask-SQLAlchemy is an extension for Flask that adds support for SQLAlchemy to your application. It aims to simplify using SQLAlchemy with Flask by providing useful defaults and extra helpers that make it easier to accomplish common tasks.
Install it:
```shell
pip install flask-sqlalchemy
```

## How to run server ?
Once you installed the modules and packages, just run the *main.py*:
```shell
python main.py
```

If everything is set correctly, you will get something like this:
```shell
 * Serving Flask app 'website' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 554-480-689
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 ```
