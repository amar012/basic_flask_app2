# from . import app
from flask import render_template, Blueprint

users_blueprint = Blueprint('users', __name__, template_folder='templates')

@users_blueprint.route('/login', methods=("GET",))
def login():
    #breakpoint()
    #return render_template('login.html')

    return render_template('login.html')