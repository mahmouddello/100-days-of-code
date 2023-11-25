from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# TODO: Create a RegisterForm to register new users

class RegisterForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired()], name="email")
    password = PasswordField(label="Password", validators=[DataRequired()], name="password")
    name = StringField(label="Name", validators=[DataRequired()], name="name")
    submit = SubmitField(label="Register")


# TODO: Create a LoginForm to login existing users
class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired()], name="email")
    password = PasswordField(label="Password", validators=[DataRequired()], name="password")
    submit = SubmitField(label="Login")


# TODO: Create a CommentForm so users can leave comments below posts
class CommentForm(FlaskForm):
    comment = CKEditorField(label="Share your thoughts", validators=[DataRequired()], name="comment")
    submit = SubmitField(label="Post Comment")
