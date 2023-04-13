from flask import Flask, render_template
from config import Config
from .site.routes import site
from .api.routes import api

from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from models import db as root_db, ma


app = Flask(__name__)
CORS(app)

app.register_blueprint(site)
app.register_blueprint(api)

app.config.from_object(Config)
root_db.init_app(app)
ma.init_app(app)
migrate = Migrate(app, root_db)