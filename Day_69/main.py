import re
from datetime import date
from functools import wraps

from flask import Flask, abort, flash, redirect, render_template, request, url_for
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import (
    LoginManager,
    UserMixin,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from werkzeug.security import check_password_hash, generate_password_hash

from forms import CommentForm, CreatePostForm, LoginForm, RegisterForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


##CONFIGURE TABLES
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), unique=True, nullable=False)
    name = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    salt = db.Column(db.String(100))
    articles = db.relationship("BlogPost", backref="author_", lazy=True)
    comments = db.relationship("Comment", backref="author_", lazy=True)

    def check_password_correction(self, attempted_password):
        return check_password_hash(self.password, attempted_password)


class BlogPost(db.Model):
    __tablename__ = "blog_posts"  # PARENT of child line 75
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(250), nullable=False)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    author_id = db.Column(db.Integer(), db.ForeignKey("user.id"))
    comments = db.Column(db.Integer(), db.ForeignKey("comment.id"))  # Link to child table line 70


class Comment(db.Model):
    __tablename__ = "comment"

    id = db.Column(db.Integer(), primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    author_name = db.Column(db.String(50), nullable=False)
    parent_post = db.Column(db.Integer(), db.ForeignKey("blog_posts.id"))  # __tablename___ (parent)line 57
    author = db.Column(db.Integer(), db.ForeignKey("user.id"))
    comment_author = db.relationship("User", backref="comment")

def hash_passwd(password):
    return generate_password_hash(password, method="pbkdf2:sha256", salt_length=8)


def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print(current_user.is_authenticated)
        if current_user.is_authenticated and current_user.id == 1:
            return f(*args, **kwargs)
        return redirect(url_for("login"))

    return decorated_function

# Gravatars
gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=True,
                    base_url=None)

@app.route("/")
def get_all_posts():
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts)


@app.route("/register", methods=["GET", "POST"])
def register():
    register_form = RegisterForm()
    if request.method == "POST" and register_form.validate_on_submit():
        if User.query.filter_by(email=request.form["email"]).first():
            flash("Email already in use.", category="error")
            next = request.args.get("next")
            return redirect(next or url_for("get_all_posts"))
        else:
            new_user = User(
                email=request.form["email"],
                name=request.form["name"],
                password=hash_passwd(request.form["password"]),
                salt=hash_passwd(request.form["password"]).split("$")[1],
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for("get_all_posts"))
    return render_template("register.html", form=register_form)


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if request.method == "POST" and login_form.validate_on_submit():
        attempted_user = User.query.filter_by(email=request.form["email"]).first()
        print(attempted_user)
        if attempted_user and attempted_user.check_password_correction(attempted_password=request.form["password"]):
            login_user(attempted_user)
            flash("Logged in successfully.", category="info")
            next = request.args.get("next")
            return redirect(next or url_for("get_all_posts"))
        else:
            flash("Logging in FAILED!.", category="error")
            return redirect(url_for("get_all_posts"))

    return render_template("login.html", form=login_form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("get_all_posts"))


@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):
    form = CommentForm()
    if request.method == "POST":
        new_comment = Comment(
            text=request.form["editor"],
            author=current_user.id,
            author_name=current_user.name,
            parent_post=post_id,
        )
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for("show_post", post_id=post_id))
    requested_post = BlogPost.query.get(post_id)
    print("FFFFFFFFFFFFFFFFFFFFFFFFFFF")
    comments = Comment.query.filter_by(parent_post=post_id).all()
    return render_template("post.html", post=requested_post, form=form, comments=comments)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    print("########")
    print(current_user.id)
    form = CreatePostForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_post = BlogPost(
                title=form.title.data,
                subtitle=form.subtitle.data,
                body=form.body.data,
                img_url=form.img_url.data,
                author=current_user.name,
                date=date.today().strftime("%B %d, %Y"),
                author_id=current_user.id,
            )
            db.session.add(new_post)
            db.session.commit()
            return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


@app.route("/edit-post/<int:post_id>")
@admin_only
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(
        title=post.title, subtitle=post.subtitle, img_url=post.img_url, author=post.author, body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = edit_form.author.data
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))

    return render_template("make-post.html", form=edit_form)


@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = BlogPost.query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for("get_all_posts"))


if __name__ == "__main__":
    app.run(debug=True)
