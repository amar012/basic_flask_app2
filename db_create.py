# db_create.py
from bfp import db
from bfp.models import Book

db.create_all()

b1 = Book('Learn Python the Easy Way', 'Computer Programming')
b2 = Book('The Omen', 'Horror')
b3 = Book('The Day Of The Jackal', 'Detective')

db.session.add(b1)
db.session.add(b2)
db.session.add(b3)

db.session.commit()