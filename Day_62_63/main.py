from operator import index

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db = SQLAlchemy(app)

# ("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=False)


db.create_all()
# new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
# db.session.add(new_book)
# db.session.commit()


def read_all_books():
    books_list = []
    lst = db.session.query(Book).all()
    for el in lst:
        books_list.append(el)
    return books_list


def remove_book(id_):    
    book_to_delete = Book.query.filter_by(id=id_).first()
    db.session.delete(book_to_delete)
    db.session.commit()


def add_new_book(form_data):
    new_book = Book(
        title=form_data["book_name"],
        author=form_data["author"],
        rating=form_data["rating"],
    )
    db.session.add(new_book)
    db.session.commit()

def find_book(id):
    return Book.query.filter_by(id=id).first()

def update_book_rating(id_, rating):
    print(id_, rating)
    book_to_update = Book.query.filter_by(id=id_).first()
    book_to_update.rating = rating
    db.session.commit()

################  Flask Routes ##############
# @app.route("/edit/<int:id_>", methods=["GET", "POST"])
# def edit(id_):
#     if request.method == "POST":
#         print("POSTING")
#         return redirect("/")
#     book = find_book(id_)
    
#     #print(book["title"])
#     return render_template("edit.html", title = book.title, rating=book.rating, id_=book.id)
@app.route("/edit/<id_>", methods=["GET", "POST"])
def edit(id_):    
    if request.method == "POST":        
        print("POSTING")
        update_book_rating(id_=id_, rating=request.form["rating"])
        return redirect("/")
    book = find_book(id_)
    return render_template("edit.html", title = book.title, rating=book.rating, id_=book.id)


@app.route("/")
def home():
    books_list = read_all_books()
    return render_template("index.html", book_list=books_list)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        data=request.form
        add_new_book(data)
        return redirect("/")
    return render_template("add.html")



@app.route("/del")
def del_book():
    remove_book(request.args.get('id_'))
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
