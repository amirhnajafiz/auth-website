from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Note
from . import db

views = Blueprint('views', __name__)  # Creating a blueprint instance



# Create a view or blueprint
@views.route('/', methods=['GET', 'POST'])
@login_required  # User can only access the home page if it is logged in
def home():  # Creating the home end-point
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:  # Content validation
            flash('Note is too short!', category='error')
        else:
            newNote = Note(data=note, user_id=current_user.id)
            db.session.add(newNote)
            db.session.commit()
            flash('Note added!', category='success')
    return render_template("home.html", user=current_user)  # Reference to current user in home page
