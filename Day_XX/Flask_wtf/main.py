
from flask import Flask, redirect, render_template, request, session, url_for
from flask_wtf import FlaskForm
from wtforms import (
    RadioField,
    SelectField,
    StringField,
    SubmitField,
    TextAreaField,
    form,
)
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"


class Widgets_add(FlaskForm):
    first_name = StringField(label="First Name")
    last_name = StringField(label="Last Name")
    rating = SelectField(
        label="How you are can rate you from 1 to 5",
        choices=[
            ("1", "1"),
            ("2", "2"),
            ("3", "3"),
            ("4", "4"),
            ("5", "5"),
        ],
    )
    comment = TextAreaField(label="Enter your comment")
    choice = RadioField(
        label="What do you like more",
        choices=[("a", "a"), ("b", "b")],
    )

    submit = SubmitField(label="Submit")


@app.route("/", methods=["GET", "POST"])
def home():
    form_ = Widgets_add()
    return render_template("index.html", form=form_)



if __name__ == "__main__":
    app.run(debug=True)
