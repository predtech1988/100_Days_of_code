from flask import Flask, render_template

from post import Post

app = Flask(__name__)

posts_data = Post()


@app.route("/")
def home():
    return render_template("index.html", blog_posts=posts_data.data)


@app.route("/post/<id>")  # Better to do @app.route("/post/<int:id>")
def go_to_blog_id(id):
    print("Go to id")
    return render_template("post.html", text=posts_data.data[int(id)])


if __name__ == "__main__":
    app.run(debug=True)
