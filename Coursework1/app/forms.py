from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, DateTimeField, TextAreaField, HiddenField, SubmitField
from wtforms.validators import DataRequired

class input_form(FlaskForm):
    id_field = HiddenField()                                                    #unique identifying id that is abstracted from the user
    title = StringField('title', validators = [DataRequired()])                 #validators method() ensures it cannot be left empty 
    module_code = StringField('module_code', validators = [DataRequired()])     #validators method() ensures it cannot be left empty 
    deadline = DateTimeField('deadline', format = '%m-%d-%y')                   #date format: month-date-year
    description = TextAreaField('description')                                  #description text-box
    submit = SubmitField('Submit')                                              #submit button