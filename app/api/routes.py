from flask import Blueprint, request, jsonify, render_template
from models import db, CalenderEvent, event_schema, events_schema

api = Blueprint('api',__name__, url_prefix='/api')

@api.route('/test')
def test():
    return {'hello':'SOLAS'}


@api.route('/event', methods = ['POST'])
def create_event():
    event = request.json['event']
    date = request.json['date']
    time = request.json['time']
    place = request.json['place']
    date_created = date_created

    event = CalenderEvent(event, date, time, place, date_created)

    db.session.add(event)
    db.session.commit()

    response = event_schema.dump(event)
    return jsonify(response)