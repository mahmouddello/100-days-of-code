import requests
from datetime import datetime
from random import randint
from flask import Flask, render_template
from genderize import Genderize

agify = "https://api.agify.io?name="

app = Flask(__name__)

genderizer = Genderize()


@app.route("/")
def home():
    number = randint(1, 10)
    year = datetime.today().year
    # how to pass this to html? after passing template in render_template()
    # flask says we can pass argument called **context which it means we can
    # pass as many keyword arguments as we want
    return render_template("index.html", num=number, year=year)


@app.route("/guess/<name>")
def guess(name):
    gender = genderizer.get1(name=name)["gender"]
    response = requests.get(f"{agify}{name}").json()
    age = response["age"]
    return render_template("index2.html", gender=gender, age=age, name=name.title())


@app.route("/blogs")
def blog():
    all_posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("blog.html", blogs=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
