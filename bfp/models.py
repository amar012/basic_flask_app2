# bfp.models.py
from . import db

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String, nullable=False)
    book_genre = db.Column(db.String, nullable=False)

    def __init__(self, book_name, book_genre):
        self.book_name = book_name
        self.book_genre = book_genre

    def __repr__(self):
        return '<title {}'.format(self.name)