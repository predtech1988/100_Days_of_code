from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, InputRequired, Length


class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(
        label="Password", validators=[InputRequired(), Length(min=8, message=u"Pasword too short")]
    )
    submit = SubmitField(label="Log In")


app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"
Bootstrap(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if request.method == "POST":
        if (
            login_form.validate_on_submit()
            and login_form.email.data == "test@bk.ru"
            and login_form.password.data == "zzzzzzzz"
        ):
            print(login_form.email.data)
            return render_template("ok.html")
        else:
            return render_template("error_403.html")
    return render_template("login.html", form=login_form)


if __name__ == "__main__":
    app.run(debug=True)
