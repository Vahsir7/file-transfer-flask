from flask import render_template, Blueprint, redirect, url_for, request
from application.models import Files
import os
from . import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            new_file = Files(file=file.filename)
            db.session.add(new_file)
            db.session.commit()
            file.save(os.path.join('application/static', file.filename))
        return render_template('home.html')
    return render_template('home.html')
