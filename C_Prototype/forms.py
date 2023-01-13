from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class SearchForm():
    keywords = StringField("Enter keywords")
    submit = SubmitField("Go")
