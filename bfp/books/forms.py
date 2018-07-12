# bfp/books/forms.py

from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class AddBookForm(Form):
    book_title = StringField('Book Name', validators=[DataRequired()])
    book_genre = StringField('Book Genre', validators=[DataRequired()])