# bfp\__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config = True)
app.config.from_pyfile('flask.cfg')

db = SQLAlchemy(app)

# from . import views

from bfp.books.views import books_blueprint
from bfp.users.views import users_blueprint

app.register_blueprint(books_blueprint)
app.register_blueprint(users_blueprint)

