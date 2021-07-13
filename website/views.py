"""views file

The endpoints of pages in our website is being handle here.

Basically it has the home route and the delete-note endpoint.
"""
from datetime import datetime
from flask import Blueprint, render_template, request, flash, jsonify
from flask.json import jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json



views = Blueprint('views', __name__)  # Creating a blueprint instance


# Create a view or blueprint
@views.route('/', methods=['GET', 'POST'])
@login_required  # User can only access the home page if it is logged in
def home(): 
    """Creating the home end-point

    The home function which renders the home page for user.
    """
    if request.method == 'POST':
        note = request.form.get('note')
        taskdate = request.form.get('taskdate')
        taskdate = datetime.strptime(taskdate, '%Y-%m-%dT%H:%M')

        if len(note) < 1:  # Content validation
            flash(message='Note is too short!', category='error')
        elif taskdate < datetime.now():
            flash(message='Due date is not valid.', category='error')
        else:
            newNote = Note(data=note, due_date=taskdate, user_id=current_user.id)
            db.session.add(newNote)
            db.session.commit()
            flash(message='Note added!', category='success')
    
    filter_key = "id"

    if request.method == 'GET':
        if 'key' in request.args:
            filter_key = request.args.get('key')

    return render_template("home.html", user=current_user, current_time=datetime.now(), filter_key=filter_key)  # Reference to current user in home page

@views.route('/delete-note', methods=['POST'])
def delete_note():
    """

    Delete note is a simple function that removes the user
    note and return nothing.

    This is a one thing doing function.
    """
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)

    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    
    return jsonify({})
