from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

from market.models import User


class RegisterForm(FlaskForm):

    def validate_user_name(self, user_name_to_check):
        user = User.query.filter_by(user_name=user_name_to_check.data).first()
        if user:
            raise ValidationError("User name already exist! Please try different username")

    def validate_email_address(self, email_to_check):
        email_address = User.query.filter_by(email_address=email_to_check.data).first()
        if email_address:
            raise ValidationError("Email already in use! Try different.")
    user_name = StringField(
        label="User Name",
        validators=[
            DataRequired(),
            Length(min=2, max=30),
        ],
    )
    email_address = StringField(
        label="Email address",
        validators=[
            DataRequired(),
            Email(),
        ],
    )
    password1 = PasswordField(
        label="Password",
        validators=[
            DataRequired(),
            Length(min=6, max=100),
        ],
    )
    password2 = PasswordField(
        label="Confirm password",
        validators=[
            EqualTo("password1"),
        ],
    )
    submit = SubmitField(label="Submit")


class LoginForm(FlaskForm):
    user_name = StringField(label="User Name", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Log in")

class PurchaseItemForm(FlaskForm):
        submit = SubmitField(label="Purchase Item")

class SellItemForm(FlaskForm):
        submit = SubmitField(label="Sell Item")

