"""models file

In here we create the models for our database.
Two main classes are Note as a task and User as a user.
"""
from . import db  # From this package (__int__) import database
from flask_login import UserMixin 
from sqlalchemy.sql import func



class Note(db.Model):  
    """Create the note model Schema

    Note has the following attributes
    @param id: is the note unique identifier
    @param data: is the content of the task or note
    @param date: is the creation time of note
    @param due_date: is the deadline of task
    @param user_id: each note is for a unique user
    """
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    due_date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):  
    """Create the user model Schema

    User model has the following attributes
    @param id: is the user unique identifier
    @param email: is the user email which is unique
    @param password: the user password that is hashed
    @param name: the user first name in our website
    @param notes: list of user notes
    """
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')

