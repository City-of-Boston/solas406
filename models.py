from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from flask_marshmallow import Marshmallow 

# set variables for class instantiation
ma = Marshmallow()
db = SQLAlchemy()


class CalenderEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String(250), nullable=False)
    date = db.Column(db.Date, nullable = False)
    time = db.Column(db.Time, nullable = False)
    place = db.Column(db.String(250), nullable = False)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

    def __repr__(self):
        return f'User {self.event} has been added to the database'


class EventSchema(ma.Schema):
    class Meta:
        fields = ['id', 'title', 'author', 'publisher', 'isbn']

event_schema = EventSchema()
events_schema = EventSchema(many = True)