import os
from flask_bootstrap import Bootstrap5
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


# 1) validators: takes a list of validator objects
# 2) DataRequired: Makes the input field required
# 3) When a form is submitted, there may be a number of errors, so a List of errors can be generated and passed over
# to our form HTML.
# as a property on the field which generated the error, e.g., form.<field>.errors

class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email(message="either @ or . missing")])
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=8, message="less than 8 chars")])
    submit = SubmitField(label="Login")


app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("FLASK_SECRET_KEY")

bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        if form.email.data == "admin@gmail.com" and form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")

    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
