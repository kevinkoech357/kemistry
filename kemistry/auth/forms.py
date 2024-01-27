from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms import validators, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp
from kemistry.models.user import User


class LoginForm(FlaskForm):
    """
    Form for user login.
    """

    identifier = StringField(
        "Username or Email", validators=[DataRequired(), Length(min=3, max=30)]
    )
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


class RegistrationForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Length(4, 55), Email()])
    username = StringField(
        "Username",
        validators=[
            DataRequired(),
            Length(3, 21),
            Regexp(
                "^[A-Za-z][A-Za-z0-9_.]*$",
                0,
                "Usernames must have only letters, " "numbers, dots or underscores",
            ),
        ],
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            EqualTo("password2", message="Passwords must match."),
        ],
    )
    confirm_password = PasswordField("Confirm password", validators=[DataRequired()])
    submit = SubmitField("Register")

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Email already registered.")

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Username already in use.")
