from flask_wtf import FlaskForm
from wtforms import Form, StringField, TextAreaField,IntegerField, SubmitField
from wtforms.validators import DataRequired

class createform(FlaskForm):
    name = TextAreaField('Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    submit = SubmitField('Submit')

def creatingform():
    return createform()