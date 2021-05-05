from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Optional, Length



# Form for taking question inputs on Course Quizzes.
class Question(FlaskForm):
    choices = RadioField('Answer', validators = [Optional()])
    answer_text = TextAreaField('Answer', validators = [Optional(), Length(max=500)])
    submit = SubmitField("Submit")