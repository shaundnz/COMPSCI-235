from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    person_id = IntegerField('Person id', [
        DataRequired(message="put something here idiot")
    ])

    submit = SubmitField('Find')