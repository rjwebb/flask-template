#flask
from flask import render_template, request, abort

#this app
from . import app, db
from .models import Thing

# Controller for listing all of the Things
@app.route("/")
def index():
    things = db.session.query(Thing).all()
    return render_template('index.html', things=things)

@app.route("/about")
def about_page():
    return render_template('about.html')

# Controller for a single Thing
@app.route("/thing/<thing_id>")
def single_thing(thing_id):
    thing = db.session.query(Thing).get(thing_id)
    if thing:
        return render_template('thing_detail.html', thing=thing)
    else:
        abort(404)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
