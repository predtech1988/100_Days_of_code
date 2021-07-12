import datetime

import requests
from flask import Flask, render_template

app = Flask(__name__)


def get_age_and_gender(name):
    url_age = "https://api.agify.io?name=" + name
    url_gender = "https://api.genderize.io?name=" + name
    age = requests.get(url=url_age).json()["age"]
    gender = requests.get(url=url_gender).json()["gender"]
    return (age, gender)


@app.route("/")
def main_page():
    resp = """
    <h1>Guess a number between 0 and 9 </h1>
    <br>
    <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" alt="numbers_gif">
    """
    current_year = datetime.datetime.now().strftime("%Y")
    return render_template(
        "index.html",
        current_year=current_year,
    )


@app.route("/guess/<user_name>")
def guess(user_name):
    age, gender = get_age_and_gender(user_name)
    return render_template("guess.html", name=user_name, gender=gender, age=age)


@app.route("/blog/<num>")
def get_blog(num):
    # url_ = "https://www.npoint.io/docs/5abcca6f4e39b4955965"
    # resp = requests.get(url=url_).json()
    resp = [
        {"id": 0, "title": "First title", "subtitle": "First sub title"},
        {"id": 1, "title": "Second title", "subtitle": "Second sub title"},
        {"id": 2, "title": "Third title", "subtitle": "Third sub title"},
    ]
    return render_template("blog.html", blog_posts=resp)


if __name__ == "__main__":
    app.run(debug=True)
