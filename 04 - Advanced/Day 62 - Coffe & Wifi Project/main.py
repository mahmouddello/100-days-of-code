import os
import csv
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("FLASK_SECRET_KEY")
bootstrap = Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired(message="Can't Be Empty")])
    location = StringField('Location', validators=[DataRequired(), URL(message="Invalid URL")])
    opening = StringField('Opening time e.g. 8AM', validators=[DataRequired(message="Can't Be Empty")])
    closing = StringField('Closing time e.g. 9PM', validators=[DataRequired(message="Can't Be Empty")])
    coffe_rating = SelectField("Coffe Rating", coerce=str,
                               choices=('☕', '☕☕', '☕☕☕', '☕☕☕☕', '☕☕☕☕☕'))

    wifi_rating = SelectField("WiFi Rating", coerce=str,
                              choices=('✘', '📶', '📶📶', '📶📶📶', '📶📶📶📶', '📶📶📶📶📶'))

    power_socket = SelectField("Power Socket", coerce=str,
                               choices=('✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'))

    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    """Adds cafe to the csv file to fetch later for different operations."""
    form = CafeForm()
    # validate the form then save the data to the csv file to render the updated version of the café list
    if form.validate_on_submit():
        print("True")
        with open("cafe-data.csv", newline='\n', mode='a', encoding='utf-8') as csv_file:
            cafe_data = [
                form.cafe.data,
                form.location.data,
                form.opening.data,
                form.closing.data,
                form.coffe_rating.data,
                form.wifi_rating.data,
                form.power_socket.data]
            csv_write = csv.writer(csv_file)
            csv_write.writerow(cafe_data)
        return redirect(url_for("cafes"))  # redirecting to the /cafes
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    """ Gets all data from the csv file, appends each row from the file as a list (Nested List),
    then sends the data to the template to handle it with Jinja. """

    # Read the csv data and the rows to a list
    with open('cafe-data.csv', newline='', encoding="utf-8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows, columns=list_of_rows[0])


if __name__ == '__main__':
    app.run(debug=True)
