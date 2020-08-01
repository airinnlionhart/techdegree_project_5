from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, IntegerField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField
#flask-wtf-0.14.3


class CreateEntryForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    timeSpent = IntegerField('timeSpent', validators=[DataRequired()])
    whatILearned = TextAreaField('whatILearned', validators=[DataRequired()])
    ResourcesToRemember = TextAreaField('ResourcesToRemember', validators=[DataRequired()])
    date = DateField('DatePicker', validators=[DataRequired()], format='%Y-%m-%d')

