from . import app
from flask import render_template

@app.route('/', methods=("GET",))
def index():
    #breakpoint()
    #return render_template('index.html')

    user = {'username': 'Miguel'}
    #return render_template('index.html', title="Home", user=user)
    return render_template('index.html')