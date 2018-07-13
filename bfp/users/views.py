# bfp/users/views.py
# from . import app
from flask import render_template, Blueprint, request, redirect, url_for, flash
from sqlalchemy.exc import IntegrityError
from bfp import db
from bfp.models import User
from .forms import RegisterUserForm

users_blueprint = Blueprint('users', __name__)

@users_blueprint.route('/login', methods=("GET",))
def login():
    #breakpoint()
    #return render_template('login.html')

    return render_template('login.html')

@users_blueprint.route('/register', methods=('GET', 'POST'))
def user_register():
    form = RegisterUserForm(request.form)

    if request.method == 'POST':
        if form.validate_on_submit():
            try:
                email = form.email.data
                password = form.password.data
                new_user = User(email, password)
                db.session.add(new_user)
                db.session.commit()
                flash('Thanks for registering', 'success')
                return redirect(url_for('books.index'))
            except IntegrityError:
                db.session.rollback()
                flash('ERROR! {} already exits'.format(email), 'error')
    return render_template('register.html', form=form)
            