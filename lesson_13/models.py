from lesson_13.orm import db
from datetime import datetime


class Guests(db.Model):
    '''
    The class describes Guests table
    '''

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.String(80), nullable=False)
    adress = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)


class GuestBookItem(db.Model):
    '''
    The class describes Guests table
    '''

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)

    message = db.Column(db.String(80), nullable=False)
    date_and_time = db.Column(db.DateTime, default=datetime.now())

    object_is_deleted = db.Column(db.Boolean, default=False, nullable=False)

    #link
    guest = db.relationship('Guests', foreign_keys=[guest_id, ])

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.guest.name,
            'email': self.guest.email,
            'age': self.message,
            'date_and_time': self.date_and_time
        }
