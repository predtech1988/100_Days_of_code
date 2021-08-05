from flask import Flask, redirect, render_template, request, session, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import BooleanField, SelectField, StringField, SubmitField, TextAreaField
from wtforms.validators import URL, DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7b"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///manga-collection.db"
db = SQLAlchemy(app)


class Manga(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    link = db.Column(db.String(250), unique=True, nullable=False)
    description = db.Column(db.String(3250), unique=True, nullable=False)
    cover_name = db.Column(db.String(250), unique=True, nullable=False)
    score = db.Column(db.Integer, unique=False, nullable=True)


# db.create_all()


def add_new_manga(form):
    new_manga = Manga(
        title=form["title"],
        link=form["link"],
        description=form["description"],
        cover_name=form["cover_name"],
        score=0,
    )
    db.session.add(new_manga)
    db.session.commit()
    return


def get_manga_list():
    manga_list = []
    lst = db.session.query(Manga).all()
    for el in lst:
        manga_list.append(el)
    return manga_list


def get_manga_by_id(id_):
    # Book.query.filter_by(title="Harry Potter").first()
    manga = db.session.query(Manga).filter_by(id_=id_).first()
    print(manga.title)


def update_manga_score(manga_list):
    for title in manga_list:
        id_ = title
        manga = Manga.query.filter_by(id_=id_).first()
        manga.score += 1
        db.session.commit()


###### WTF Form's ########
class AddForm(FlaskForm):
    title = StringField("Manga Title", validators=[DataRequired()])
    link = StringField("Link", validators=[DataRequired(), URL(require_tld=True, message="Wrong URL format!")])
    description = TextAreaField("Description", validators=[DataRequired()])
    cover_name = StringField("Cover file name", validators=[DataRequired()])
    # score = BooleanField("Like")
    submit = SubmitField(label="Submit")


class MangaVote(FlaskForm):
    vote = BooleanField()
    submit = SubmitField(label="Submit")


############## Flask routes #######


@app.route("/add_manga", methods=["GET", "POST"])
def add_manga():
    form_ = AddForm()
    if request.method == "POST":
        data = request.form
        add_new_manga(data)
        return redirect("/add_manga")
    return render_template("add.html", form=form_)


@app.route("/vote", methods=["GET", "POST"])
def vote():
    if request.method == "POST":
        manga_to_update = request.form.getlist("manga.id_")
        if manga_to_update:
            update_manga_score(manga_to_update)
    form_ = MangaVote()
    manga_list = get_manga_list()
    return render_template("vote.html", manga_list=manga_list, form=form_)


if __name__ == "__main__":
    app.run(debug=True)
