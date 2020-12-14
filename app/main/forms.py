from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from wtforms import validators
from app.models import User

class AddForm(FlaskForm):
    body = TextAreaField('Pitch', [validators.optional(), validators.length(max=200)])
    category = SelectField('Category', choices=[( 'pickup', 'Pickup Lines'), ('interview', 'Interview'), ('product', 'Product'), ('promotion', 'Promotion')])
    submit = SubmitField('Submit')

class AddCommentForm(FlaskForm):
    body = TextAreaField('Comment', [validators.optional(), validators.length(max=200)])
    submit = SubmitField('Submit')
