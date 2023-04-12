from flask import Blueprint, render_template, request
from models import db, CalenderEvent

site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/calender')
def calender():
    return render_template('calender.html')

@site.route('/admin')
def admin():
    return render_template('admin.html')