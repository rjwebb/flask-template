from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

import os

# Initialise the Flask web application
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

import controllers
import filters
