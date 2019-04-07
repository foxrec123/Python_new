from wtforms import IntegerField, validators, StringField
from flask_wtf import FlaskForm

class GuestBookForm(FlaskForm):
    guest_id = IntegerField('guest_id', [validators.DataRequired()])
    message = StringField('message', [validators.Length(min=6), validators.DataRequired()])