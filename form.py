from flask_wtf import FlaskForm
from wtforms import Form, StringField, TextAreaField,IntegerField, SubmitField
from wtforms.validators import DataRequired

class createform(FlaskForm):
    name = TextAreaField('Description', validators=[DataRequired()])
    age = IntegerField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')


    