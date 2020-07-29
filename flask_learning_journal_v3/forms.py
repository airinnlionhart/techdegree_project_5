from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, IntegerField, DateField
from wtforms.validators import data_required
#flask-wtf-0.14.3

class JournalEntryForm(FlaskForm):
    journal_title = StringField(
        'journal_title',
        validators=[
            data_required()
        ]
    )
    time_spent = IntegerField(
        'time_spent',
        validators=[
            data_required()
        ]
    )
    learned = TextAreaField(
        'learned',
        validators=[
            data_required()
        ]
    )
    remember = TextAreaField(
        'remember',
        validators=[
            data_required()
        ]
    )
    date_time = DateField(
        'date_time',
        validators=[
            data_required()
        ]
    )

class CreateEntryForm(FlaskForm):
    journal_title = StringField('journal_title', validators=[data_required()])
    time_spent = IntegerField('time_spent', validators=[data_required()])
    learned = TextAreaField('learned', validators=[data_required()])
    remember = TextAreaField('remember', validators=[data_required()])
    date_time = DateField('date_time', validators=[data_required()], format='%m/%d/%Y')