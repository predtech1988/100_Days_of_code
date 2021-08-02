from flask_wtf import form

try:
    from flask import Flask, redirect, render_template, request, session, url_for
    from flask_wtf import FlaskForm
    from wtforms import StringField, SubmitField
    from wtforms.validators import DataRequired
except ImportError:
    print("Error while importing modules")

app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"

class Widgets_add(FlaskForm):
    name = StringField(label="Book Name")
    author = StringField(label="Author")
    rating = StringField(label="Rating")
    submit = SubmitField(label="Add Book")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add")
def add_book():
    add_book_form = Widgets_add()
    return render_template("add.html", form = add_book_form)

if __name__ == "__main__":
    app.run(debug=True)
