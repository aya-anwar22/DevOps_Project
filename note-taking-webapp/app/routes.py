from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Note
from app import db

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        if title or content:
            note = Note(title=title, content=content)
            db.session.add(note)
            db.session.commit()
        return redirect(url_for('main.index'))

    notes = Note.query.order_by(Note.created_at.desc()).all()
    return render_template('index.html', notes=notes)
