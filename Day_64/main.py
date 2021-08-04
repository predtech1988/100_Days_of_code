import requests
from flask import Flask, redirect, render_template, request, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies-collection.db"
Bootstrap(app)
db = SQLAlchemy(app)

########### DB Model ############
class Movie(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1250), nullable=False)
    rating = db.Column(db.Float(250), nullable=False)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)


###############################


########### WTF Forms ############
class EditForm(FlaskForm):
    rating =FloatField ("Your rating Out of 10 ege: 7.5", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField(label="Done")

class AddMovie(FlaskForm):
    title =StringField ("Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Add")

###################################
# db.create_all()
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# db.session.add(new_movie)
# db.session.commit()
def get_movies_list():
    movies_list = []
    lst = db.session.query(Movie).all()
    for el in lst:
        movies_list.append(el)
    return movies_list

def get_movie_data(title):
    pass
def get_movie_by_id(id_):
    return db.session.query(Movie).filter_by(id_=id_).first()


def update_movie(id_, data):
    movie_to_update = Movie.query.filter_by(id_=id_).first()
    movie_to_update.rating = data["rating"]
    movie_to_update.review = data["review"]
    db.session.commit()

def delete_movie(id_):
    movie_to_delete = Movie.query.get(id_)
    db.session.delete(movie_to_delete)
    db.session.commit()
############### Flask Routes ###############
# @app.route("/")
# def home():
#     movies = get_movies_list()
#     return render_template("index.html", movies=movies)

@app.route("/")
def home():
    code_verifier = code_challenge = "k2oDwJxT8paNY1JwtNxRbS8yotMo8nc3C66AGAcNBtevi3-Kxz8sShBexxJarvxXpFnMUGVXJc9p4f27ZhdQ0LVX-wOBFusqCBfeLXhRbS1MyJMn-JRihVEIoupScbk"
    import requests  # Importing module

    STOCK = "TSLA"  # Set constatn var 
    API_URL = "https://myanimelist.net/v1/oauth2/authorize"   # API endpoint
    API_KEY = "09CN7MDZJTQKKB4U"    # API key

    # Creating dic with explicit type annotation
    parameteres = {
        "response_type": "code",
        "client_id": "412ac077d2f7ff148be33d2ffe97b854",
        "code_challenge": code_challenge,
        
    }

    response = requests.get(url=API_URL, params=parameteres)
    raw_data = response.content
    print(raw_data)
    return raw_data



@app.route("/edit/<int:id_>", methods=["GET", "POST"])
def edit(id_):
    if request.method == "POST":
        print("POSTING ^^^^^^^^^^^^^^^^^^^^^^")
        update_movie(id_, request.form)
        return redirect("/")
    movie = get_movie_by_id(id_)
    edit_form = EditForm()
    return render_template("edit.html", movie=movie, form=edit_form)


@app.route("/delete")
def delete():
    movie_id = request.args.get("id_")
    delete_movie(movie_id)    
    return redirect("/")


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        movie_title = request.form["title"]
        print(movie_title)
        return redirect("/")
    form_ = AddMovie()    
    return render_template("add.html", form=form_)

if __name__ == "__main__":
    app.run(debug=True)
