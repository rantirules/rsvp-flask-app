from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length

class AddCharacterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])
    age = IntegerField('Age', validators=[DataRequired()])
    catch_phrase = StringField('Catch phrase', validators=[DataRequired(), Length(min=2, max=100)])
    submit = SubmitField('Add Character')