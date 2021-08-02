<<<<<<< HEAD
import csv

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import URL, DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField("Cafe name", validators=[DataRequired()])
    location = StringField("Location", validators=[
        DataRequired(),
        URL(require_tld=True, message="Wrong URL format!")
        ])
    opening_time = StringField("Opening time", validators=[DataRequired()])
    closing_time = StringField("Closing time", validators=[DataRequired()])
    coffee_rating =SelectField("Coffee Rating",
        choices=[
            ("☕️", "☕️"),
            ("☕️☕️", "☕️☕️"),
            ("☕️☕️☕️", "☕️☕️☕️"),
            ("☕️☕️☕️☕️", "☕️☕️☕️☕️"),
            ("☕️☕️☕️☕️☕️", "☕️☕️☕️☕️☕️"),
        ],
    )
    wifi_rating =SelectField("WiFI Rating",
        choices=[
            ("✘", "✘"),
            ("💪", "💪"),
            ("💪💪", "💪💪"),
            ("💪💪💪", "💪💪💪"),
            ("💪💪💪💪", "💪💪💪💪"),
            ("💪💪💪💪💪", "💪💪💪💪💪"),
        ],
    )
    power_socket_rating = SelectField("Power socket Rating",
        choices=[
            ("✘", "✘"),
            ("🔌", "🔌"),
            ("🔌🔌", "🔌🔌"),
            ("🔌🔌🔌", "🔌🔌🔌"),
            ("🔌🔌🔌🔌", "🔌🔌🔌🔌"),
            ("🔌🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"),
        ],
    )
    submit = SubmitField("Submit")


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------
def save_data(data):
    with open("./Day_61/cafe-data.csv", "a", newline='') as f:
        write = csv.writer(f)
        #write.writerow("\n")
        write.writerow(data)


def form_handler(form):
    """
    Takes data from the form, conwert it before writing in csv
    """
    csv_line = []
    # csv_line.append()
    # print(form.cafe.data)
    
    for field_name, dat in form.data.items():
        if field_name != "submit" and field_name != "csrf_token":
            csv_line.append(dat)
    #print(csv_line)
    save_data(csv_line)

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        form_handler(form)
        return" <h1>Send successfully</h1> <br><a href='/'>Main page</a>"
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template("add.html", form=form)


@app.route("/cafes")
def cafes():
    with open("./Day_61/cafe-data.csv", newline="") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=",")
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template("cafes.html", cafes=list_of_rows)


if __name__ == "__main__":
    app.run(debug=True)
||||||| a7f8efd
=======
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
>>>>>>> 6cc100170dae1652de0068cf9db43e9b6446f32e
