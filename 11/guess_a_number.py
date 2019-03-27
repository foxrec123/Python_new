from flask import Flask, request
import random
from wtforms import IntegerField, validators
from flask_wtf import FlaskForm
import os

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='This key must be secret!',
    WTF_CSRF_ENABLED=False

)

class ContactForm(FlaskForm):
    number = IntegerField('Number', [
        validators.DataRequired()
    ])


class Guesser(object):
    number = 0
    @classmethod
    def set_number(cls):
        cls.number = random.randint(0, 100)
        print(Guesser.number)

    @classmethod
    def compare_number(cls, entered_number):
        if entered_number > cls.number:
            return '>'
        elif entered_number < cls.number:
            return '<'
        else:
            return '='


@app.route('/',  methods=['GET'])
def home():
    Guesser.set_number()
    return 'A Number has been set'

@app.route('/guess',  methods=['POST'])
def guess():
    form = ContactForm(request.form)
    if form.validate():
         sign = Guesser.compare_number(form.number.data)
         if sign == '=':
            Guesser.set_number()
            return 'You guessed! A new number has been set'
         else:
            return sign
    else:
        return '', 404


if __name__ == '__main__':
    random.seed(os.environ['FLASK_RANDOM_SEED'])
    app.run()