import flask
from flask import Flask

app = Flask(__name__)


def style_decorator(function):
    def wrapper():
        return "<b>" + function() + "</b>"

    return wrapper


@app.route("/")
@style_decorator
def hello_world():
    return "Test string"


if __name__ == "__main__":
    app.run(debug=True)
