from flask import Flask, render_template
from config import Config
from .site_templates.routes import site

from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(site)
