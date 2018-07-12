# bfp/books/views.py

from flask import render_template, Blueprint, request, url_for, redirect, flash
from bfp import db
from bfp.models import Book
from .forms import AddBookForm


books_blueprint = Blueprint('books', __name__, template_folder='templates')

####################################
#	Helper Functions
###################################

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" %(
			getattr(form, field).label.text, error), "info")

@books_blueprint.route('/', methods=("GET",))
def index():
    #breakpoint()
    all_books = Book.query.all()
    return render_template('books.html', books=all_books)

@books_blueprint.route('/add', methods=('GET','POST',))
def add_book():
    form = AddBookForm(request.form)
    
    if request.method == 'POST':
        if form.validate_on_submit():
            new_book = Book(form.book_title.data, form.book_genre.data)
            db.session.add(new_book)
            db.session.commit()
            flash("New Book, {}, added!".format(new_book.book_name), "success")
            return redirect(url_for('books.index'))
        else:
            flash_errors(form)
            flash("ERROR! Book was not added", "error")
        
    return render_template('add_book.html', form=form)