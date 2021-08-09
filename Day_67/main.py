import datetime
import re

from flask import Flask, redirect, render_template, request, url_for
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor, CKEditorField
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import URL, DataRequired

## Delete this code:
# import requests
# posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
ckeditor = CKEditor()
ckeditor.init_app(app)
Bootstrap(app)

##CONNECT TO DB
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


## DB Methods
def get_all_posts_db():
    return db.session.query(BlogPost).all()


def get_post_by_id(id_):
    return BlogPost.query.filter_by(id=id_).first()


def add_new_post(request):
    time_now = datetime.datetime.now().strftime("%B %-d, %Y")
    new_blog_post = BlogPost(
        title=request.form["title"],
        subtitle=request.form["subtitle"],
        date=time_now,
        body=request.form["ckeditor"],
        author=request.form["author"],
        img_url=request.form["img_url"],
    )
    db.session.add(new_blog_post)
    db.session.commit()
    db.session.close()


def update_post_by_id(id_, form_data):
    post = BlogPost.query.filter_by(id=id_).first()
    post.title = form_data.form["title"]
    post.subtitle = form_data.form["subtitle"]
    post.body = form_data.form["ckeditor"]
    post.author = form_data.form["author"]
    post.img_url = form_data.form["img_url"]
    db.session.commit()
    db.session.close()
    return


def delete_post_by_id(id_):
    post_to_delete = BlogPost.query.filter_by(id=id_).first()
    db.session.delete(post_to_delete)
    db.session.commit()
    db.session.close()
    return


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = StringField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route("/")
def get_all_posts():
    posts = get_all_posts_db()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = get_post_by_id(index)
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/new-post", methods=["POST", "GET"])
def new_post_page():
    if request.method == "POST":
        add_new_post(request)
        return redirect("/")
    table = CreatePostForm()
    return render_template("make-post.html", form=table)


@app.route("/edit_post", methods=["GET", "POST"])
def edit_post():
    if request.method == "POST":
        print("POSTI")
        update_post_by_id(request.args["post_id"], request)
        return redirect(f"/post/{request.args['post_id']}")
    post_to_edit = get_post_by_id(request.args["post_id"])
    print(post_to_edit.title)
    edit_form = CreatePostForm(
        title=post_to_edit.title,
        subtitle=post_to_edit.subtitle,
        body=post_to_edit.body,
        ckeditor=post_to_edit.body,
        author=post_to_edit.author,
        img_url=post_to_edit.img_url,
    )
    return render_template("/make-post.html", form=edit_form, is_edit=True)


@app.route("/delete/<int:post_id>")
def delete_post(post_id):
    delete_post_by_id(post_id)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
