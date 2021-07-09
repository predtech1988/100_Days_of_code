from random import randint

from flask import Flask

app = Flask(__name__)

rand_number = randint(0, 9)
print(rand_number)


@app.route("/")
def main_page():
    resp = """
    <h1>Guess a number between 0 and 9 </h1>
    <br>
    <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" alt="numbers_gif">
    """
    return resp


@app.route("/<int:post_id>")
def show_post(post_id):
    correct_answer = """
        <h1 style="color: aquamarine;">Congrats! You win!!!</h1>
        <img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" alt="correct">
    """
    high = """
        <h1 style="color: red;">Too High!!!</h1>
        <img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" alt="high">
    """
    low = """
        <h1 style="color: green;">Too Low!!!</h1>
        <img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" alt="low">
    """
    if post_id == rand_number:
        return correct_answer
    if post_id < rand_number:
        return low
    else:
        return high


if __name__ == "__main__":
    app.run(debug=True)
