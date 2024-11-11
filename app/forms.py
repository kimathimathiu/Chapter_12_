from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from app.models import User
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('Password' , validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('Password' , validators=[DataRequired()])
    confirmpassword = PasswordField('Confirm Password' , validators=[DataRequired(), EqualTo('password')])
    email = StringField('Email', validators=[DataRequired(), Email()] )
    submit = SubmitField('Register')

    def validate_username(self,username):
        """Validate new username"""
        user= User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Username is already in use. Please use a different username.')

    def validate_email(self, email):
        """Validate new username"""
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use another email.')


class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 64)])
    about_me = StringField('Bio:', validators=[Length(min=0, max=200)])
    submit = SubmitField('Edit Profile')

    def __init__(self, original_username, *args, **kwargs)-> None:
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data !=self.original_username:
            user = User.query.filter_by(username= self.username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.')


class PostForm(FlaskForm):
    """Comment Form"""
    body = TextAreaField('Body', validators=[DataRequired()])
    submit = SubmitField('Post')