from flask import Flask, render_template

from post import Post

app = Flask(__name__)
posts_data = Post()


@app.route("/")
def main_page():
    return render_template("index.html", blog_posts=posts_data.data)


@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/contact")
def contact_page():
    return render_template("contact.html")


@app.route("/post/<int:post_id>")
def post_page(post_id):
    return render_template("post.html", post=posts_data.data[post_id])


if __name__ == "__main__":
    app.run(debug=True)
