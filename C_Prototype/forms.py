from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    keywords = StringField("Enter Keywords", validators=[DataRequired()])
    submit = SubmitField("")