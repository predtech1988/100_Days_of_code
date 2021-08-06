from random import randint

from flask import Flask, json, jsonify, render_template, request
from flask.wrappers import Response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy.orm import session
from werkzeug.utils import redirect

app = Flask(__name__)

##Connect to Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


##### Functions ####


def random_cafe():
    total_cafes = db.session.query(Cafe.id).count()
    # print(dir(total_cafes.value))
    rnd_id = randint(1, total_cafes)
    rnd_cafe = Cafe.query.filter_by(id=rnd_id).first()
    return jsonify(
        name=rnd_cafe.name,
        map_url=rnd_cafe.map_url,
        img_url=rnd_cafe.img_url,
        location=rnd_cafe.location,
        seats=rnd_cafe.seats,
        has_toilet=rnd_cafe.has_toilet,
        has_wifi=rnd_cafe.has_wifi,
        has_sockets=rnd_cafe.has_sockets,
        can_take_calls=rnd_cafe.can_take_calls,
        coffee_price=rnd_cafe.coffee_price,
    )


def all_cafes():
    all_cafes_list = db.session.query(Cafe).all()
    # all_cafes_dict = {}
    # for cafe in all_cafes_list:
    #     all_cafes_dict[cafe.id] = cafe.to_dict()
    # print(all_cafes_dict)
    # return all_cafes_dict
    answer = []
    for cafe in all_cafes_list:
        answer.append(cafe.to_dict())
    return jsonify(answer)


def find_cafe_by_location(cafe_loc):
    cafe = Cafe.query.filter_by(location=cafe_loc.title()).first()
    if cafe:
        return jsonify(cafe.to_dict())
    return jsonify(error={"Not Found": "Sorry location not found!"})


def add_new_cafe(args):
    new_cafe = Cafe(
        name=args["name"],
        map_url=args["map_url"],
        img_url=args["img_url"],
        location=args["location"],
        seats=args["seats"],
        has_toilet=int(args["has_toilet"]),
        has_wifi=int(args["has_wifi"]),
        has_sockets=int(args["has_sockets"]),
        can_take_calls=int(args["can_take_calls"]),
        coffee_price=args["coffee_price"],
    )
    db.session.add(new_cafe)
    db.session.commit()
    # print(new_cafe.name)
    # print(new_cafe.__dict__)
    # i = 0
    # for key, item in new_cafe.__dict__.items():
    #     if i ==0:
    #         i+=1
    #         continue
    #     print(key, item)
    #     i+=1
    return jsonify(response={"success": "Successfully added the new cafe."})


def update_coffee_price(id: int, new_price: str) -> Response:
    cafe = Cafe.query.filter_by(id=id).first()
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        db.session.close()
        return jsonify(response={"success": "Successfully updated coffee price."})
    return jsonify(response={"error": f"Cafe with id={id} not found!"})


def remove_cafe(id: int) -> Response:
    cafe = Cafe.query.filter_by(id=id).first()
    if cafe:
        db.session.delete(cafe)
        db.session.commit()
        db.session.close()
        return jsonify(response={"success": "Successfully removed cafe."})
    return jsonify(response={"error": f"Cafe with id={id} not found!"})


############# Flask routes #####
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random", methods=["GET"])
def random_cafe_page():
    if request.method == "GET":
        return random_cafe()
    return render_template("index.html")


@app.route("/all", methods=["GET"])
def all_cafes_page():
    if request.method == "GET":
        return all_cafes()
    return render_template("index.html")


@app.route("/search", methods=["GET"])
def search_page():
    par = request.args.get("loc")
    if par:
        print("params")
        return find_cafe_by_location(par)
        # print(request.url)
    # if request.method == "GET":
    #     return all_cafes()
    return render_template("index.html")


@app.route("/add", methods=["POST"])
def add_cafe_page():
    # print(request.form)
    # print(f"Args count: {len(request.form)} ")
    if len(request.form) != 10:
        return jsonify(response={"error": "Not enough arguments, needed 10"})
    return add_new_cafe(request.form)


@app.route("/update_price/<int:id>", methods=["PATCH"])
def update_price_page(id):
    # print(id)
    # print(request.form["new_price"])
    return update_coffee_price(id=id, new_price=request.form["new_price"])


@app.route("/report-closed/<int:id>", methods=["DELETE"])
def report_closed_page(id):
    # print(request.args.keys())
    if "api_key" in request.args.keys() and request.args["api_key"] == "secret_api_key":
        print("OK api key good")
        return remove_cafe(id)
    return jsonify(response={"error": "wrong API key"})


#############
#############

## HTTP GET - Read Record

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == "__main__":
    app.run(debug=True)
