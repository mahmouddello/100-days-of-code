import requests
from flask import Flask, render_template

app = Flask(__name__)
all_posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()


@app.route("/")
def home():
    return render_template("index.html", blogs=all_posts)


@app.route("/posts/<int:post_id>")
def get_blog(post_id):
    blog_data = {}
    for blog in all_posts:
        if blog["id"] == post_id:
            blog_data = {
                "title": blog["title"],
                "subtitle": blog["subtitle"],
                "body": blog["body"]
            }
            break
    return render_template("blog.html", data=blog_data)


if __name__ == "__main__":
    app.run()
