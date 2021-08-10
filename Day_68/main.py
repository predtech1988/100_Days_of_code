import os

from flask import (
    Flask,
    flash,
    redirect,
    render_template,
    request,
    send_from_directory,
    url_for,
)
from flask_login import (
    LoginManager,
    UserMixin,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()

## DB Methods
def add_new_user(data):
    new_user = User(
        name=request.form["name"],
        email=request.form["email"],
        password=request.form["password"],
    )
    db.session.add(new_user)
    db.session.commit()
    db.session.close()


@app.route('/')
def home():
    print (os.getcwd())
    # ass = os.path.join(app.root_path, 'static/files')
    # print(ass)
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        add_new_user(request)
        # new = User(
        #     name=request.form["name"],
        #     email=request.form["email"],
        #     password=request.form["password"],
        # )
        return render_template("secrets.html", user_name=request.form["name"])
    return render_template("register.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/secrets')
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
def logout():
    pass


@app.route('/download/<path:file_name>')
def download(file_name):
    return send_from_directory(directory="static/files", path=file_name)


if __name__ == "__main__":
    app.run(debug=True)
