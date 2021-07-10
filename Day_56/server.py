from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main_page():
    resp = """
    <h1>Guess a number between 0 and 9 </h1>
    <br>
    <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" alt="numbers_gif">
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
