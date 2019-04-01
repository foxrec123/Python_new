from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import date

import lesson_13.config as config


from sqlalchemy.sql import func

app = Flask(__name__)
app.config.update(config)

db = SQLAlchemy(app)

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
    date_and_time = db.Column(db.Date, default=date.today)

    object_is_deleted = db.Column(db.Boolean, default=True, nullable=False)

    #link
    guest = db.relationship('Guests', foreign_keys=[guest_id, ])

#main program
if __name__ == '__main__':

    people = GuestBookItem.query.join(Guests, Guests.id == GuestBookItem.guest_id).all()

    for p in people:
       print(p.guest.name, ' ', p.message, ' ', p.date_and_time)

    #app.run()