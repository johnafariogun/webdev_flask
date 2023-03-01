from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from log.models import User



class RegisterForm(FlaskForm):

    def validate_username(self, username_):
        user = User.query.filter_by(username=username_.data).first()
        if user:
            raise ValidationError('Username is already in the database')

    def validate_email(self, email_):
        user = User.query.filter_by(email=email_.data).first()
        if user:
            raise ValidationError('Email is already in the database')

    username = StringField(label='username', validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label='email', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='password1', validators=[Length(min=8), DataRequired()])
    password2 = PasswordField(label='password2', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='sign up')


class LoginForm(FlaskForm):
    username = StringField(label='username', validators=[DataRequired()])
    password = PasswordField(label='password', validators=[ DataRequired()])
    submit = SubmitField(label='login')
