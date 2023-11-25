import requests
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
all_posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()


@app.route("/")
def index():
    return render_template("index.html", blogs=all_posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/posts/<int:post_id>")
def post(post_id):
    blog_data = {}
    for blog in all_posts:
        if blog["id"] == post_id:
            blog_data = {
                "title": blog["title"],
                "subtitle": blog["subtitle"],
                "body": blog["body"]
            }
            break
    return render_template("post.html", data=blog_data)


@app.route("/form-entry", methods=["POST"])
def receive_date():
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    message = request.form["message"]
    print(f"{name}\n{email}\n{phone}\n{message}")
    return "<h1>Successfully sent the message</h1>"


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return contact_get()
    else:
        return redirect(url_for("receive_date"))


@app.get("/contact")
def contact_get():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run()
