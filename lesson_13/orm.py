from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

import lesson_13.config as config
from datetime import datetime

# from sys import path
# path.append('C:/Иван/Python/New_homework/lesson_13')

from sqlalchemy.sql import func

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)

@app.route('/', methods=['GET'])
def index():
    from lesson_13.models import GuestBookItem, Guests

    people = GuestBookItem.query.join(Guests, Guests.id == GuestBookItem.guest_id).all()
    return jsonify([p.to_dict() for p in people])


@app.route('/create', methods=['POST'])
def add_record():
    from lesson_13.models import GuestBookItem
    from lesson_13.forms import GuestBookForm

    form = GuestBookForm(request.form)

    if form.validate():

        person = GuestBookItem(guest_id=form.guest_id.data,
                               message=form.message.data)
        db.session.add(person)
        db.session.commit()

        return 'Record has added! {}'.format(datetime.now())
    else:
        print(type(form.errors))
        return jsonify(form.errors)


if __name__ == '__main__':

    app.run()