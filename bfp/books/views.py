# from . import app
from flask import render_template, Blueprint

books_blueprint = Blueprint('books', __name__, template_folder='templates')

@books_blueprint.route('/', methods=("GET",))
def index():
    #breakpoint()
    #return render_template('index.html')

    #user = {'username': 'Miguel'}
    #return render_template('index.html', title="Home", user=user)
    return render_template('index.html')