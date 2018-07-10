# from . import app
from flask import render_template, Blueprint
from bfp.models import Book

books_blueprint = Blueprint('books', __name__, template_folder='templates')

@books_blueprint.route('/', methods=("GET",))
def index():
    #breakpoint()
    all_books = Book.query.all()
    return render_template('books.html', books=all_books)