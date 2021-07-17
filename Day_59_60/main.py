# https://gist.github.com/discover
#C:\Users\admin\Py\cour\map>python -m venv .venv 
#cd .venv
#Scripts\activate.bat
from flask import Flask, render_template, request

from post import Post

app = Flask(__name__)
posts_data = Post()


@app.route("/")
def main_page():
    return render_template("index.html", blog_posts=posts_data.data)


@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/contact", methods=['GET', 'POST'])
def login_page():
    if request.method == "GET":
        return contact_page()
    elif request.method =="POST":
        print(request.form["name"])
        print(request.form["email"])    
        return render_template("form-entry.html", message ="Success")



@app.route("/contact")
def contact_page():
    return render_template("contact.html")


@app.route("/post/<int:post_id>")
def post_page(post_id):
    return render_template("post.html", post=posts_data.data[post_id])


if __name__ == "__main__":
    app.run(debug=True)
