import os

from flask import (
    Flask,
    flash,
    get_flashed_messages,
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

login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"
##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    salt = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    
    
    # def __repr__(self):
    #     return '<User %r>' % self.username

    def check_password_correction(self, attempted_password):
        return check_password_hash(self.password, attempted_password)



#Line below only required once, when creating DB.
#db.create_all()

## DB Methods
def add_new_user(data):
    # print(request.form)
    is_user_exists = User.query.filter_by(email=request.form["email"]).first()
    print("FFFFFFFFFFFFFFFFFFFFFFFFFFF")
    print(is_user_exists)
    if is_user_exists:
        flash("Email already in use", category="danger")
        return False  
    else:
        new_user = User(
            name=request.form["name"],
            email=request.form["email"],
            password=hash_passwd(request.form["password"]),
            salt=hash_passwd(request.form["password"]).split("$")[1],
        )
        db.session.add(new_user)
        db.session.commit()
        db.session.close()
        flash('Registered successfully.',category="info")
        return True


## Functions
def hash_passwd(password):
    return generate_password_hash(
        password,
        method="pbkdf2:sha256",
        salt_length=8
        )


## Routes
@app.route('/')
def home():
    print (os.getcwd())
    # ass = os.path.join(app.root_path, 'static/files')
    # print(ass)
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        if add_new_user(request):
            return render_template("secrets.html", user_name=request.form["name"])
    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        attempted_user = User.query.filter_by(email=request.form["email"]).first()
        #print(attempted_user.is_authenticated)
        if attempted_user and attempted_user.check_password_correction(attempted_password=request.form["password"]):
            login_user(attempted_user)
            flash('Logged in successfully.',category="info")
            next = request.args.get('next')
            return redirect(next or url_for('secrets'))
        else:
            flash('Logging in FAILED!.',category="error")
            return redirect(url_for("home"))

    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    print(current_user)

    return render_template("secrets.html", user_name=current_user.name)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route('/download/<path:file_name>')
@login_required
def download(file_name):
    return send_from_directory(directory="static/files", path=file_name)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


if __name__ == "__main__":
    app.run(debug=True)
