import os
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date
from dotenv import load_dotenv

load_dotenv("../../.env")

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("FLASK_SECRET_KEY")
Bootstrap5(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy()
db.init_app(app)

ckeditor = CKEditor()
ckeditor.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


class CreatePostForm(FlaskForm):
    title = StringField(label="Blog Post Title", validators=[DataRequired()], name="title")
    subtitle = StringField(label="Subtitle", validators=[DataRequired()], name="subtitle")
    name = StringField(label="Your Name", validators=[DataRequired()], name="name")
    url = StringField(label="Blog Image URL", validators=[DataRequired(), URL()], name="url")
    content = CKEditorField(label="Blog Content", validators=[DataRequired()], name="content")
    submit = SubmitField(label="Submit Post")


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    result = db.session.execute(db.select(BlogPost))
    posts = [post for post in result.scalars().all()]  # fetch all posts from the database
    print(posts)
    return render_template("index.html", all_posts=posts)


# TODO: Add a route so that you can click on individual posts.
@app.route('/posts/<int:post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route("/new-post", methods=["GET", "POST"])
def add_new_post():
    blog_post_form = CreatePostForm()
    if request.method == "POST":
        submitted_form = request.form
        today = date.today().strftime("%B, %Y")
        new_post = BlogPost(
            title=submitted_form["title"],
            subtitle=submitted_form["subtitle"],
            date=today,
            body=submitted_form["content"],
            author=submitted_form["name"],
            img_url=submitted_form["url"]
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", action="add", form=blog_post_form)


# TODO: edit_post() to change an existing blog post
@app.route("/edit/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        url=post.img_url,
        name=post.author,
        content=post.body
    )
    if request.method == "POST":
        post.title = request.form["title"]
        post.body = request.form["content"]
        post.author = request.form["name"]
        post.img_url = request.form["url"]
        post.subtitle = request.form["subtitle"]
        db.session.commit()
        return redirect(url_for("show_post", post_id=post_id))
    # action is used to know what is operation. Edit or New Post because both use same functionality
    return render_template("make-post.html", action="edit", form=edit_form)


# TODO: delete_post() to remove a blog post from the database
@app.route("/delete/<int:post_id>")
def delete_post(post_id):
    post = db.get_or_404(BlogPost, post_id)  # get post from database
    db.session.delete(post)
    db.session.commit()  # commit the changes
    return redirect(url_for("get_all_posts"))


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
