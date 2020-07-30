from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, IntegerField, DateField
from wtforms.validators import DataRequired
#flask-wtf-0.14.3

class JournalEntryForm(FlaskForm):
    title = StringField(
        'title',
        validators=[
            DataRequired()
        ]
    )
    timeSpent = IntegerField(
        'timeSpent',
        validators=[
            DataRequired()
        ]
    )
    whatILearned = TextAreaField(
        'whatILearned',
        validators=[
            DataRequired()
        ]
    )
    ResourcesToRemember = TextAreaField(
        'ResourcesToRemember',
        validators=[
            DataRequired()
        ]
    )
    date = DateField(
        'date',
        validators=[
            DataRequired()
        ]
    )

class CreateEntryForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    timeSpent = IntegerField('timeSpent', validators=[DataRequired()])
    whatILearned = TextAreaField('whatILearned', validators=[DataRequired()])
    ResourcesToRemember = TextAreaField('ResourcesToRemember', validators=[DataRequired()])
    date = DateField('date', validators=[DataRequired()], format='%Y-%m-%d')