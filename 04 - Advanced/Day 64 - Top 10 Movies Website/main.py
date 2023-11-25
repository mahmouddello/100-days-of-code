import os
import tmdbsimple as tmdb
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from dotenv import load_dotenv

load_dotenv("../../.env")

TMDB_BASE_IMAGE_URL = "https://image.tmdb.org/t/p/original"
tmdb.API_KEY = os.getenv("TMDB_API_KEY")
tmdb.REQUESTS_TIMEOUT = (2, 5)  # seconds, for connecting and read specifically

db = SQLAlchemy()
movies = []


class UpdateForm(FlaskForm):
    new_rating = StringField(label="Your Rating Out Of 10 e.g. 7.5", validators=[DataRequired()], name="new_rating")
    new_description = StringField(label="Your Review", validators=[DataRequired()], name="new_description")
    submit = SubmitField(label="Update")


class AddMovieForm(FlaskForm):
    movie_title = StringField(label="Movie Title", validators=[DataRequired()], name="movie_title")
    submit = SubmitField(label="Add Movie")


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), unique=True, nullable=False)


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("FLASK_SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-movies.db"
Bootstrap5(app)

db.init_app(app)

with app.app_context():
    db.create_all()

with app.app_context():
    all_movies = Movie.query.all()
    for movie in all_movies:
        movie_data = {
            "id": movie.id,
            "title": movie.title,
            "year": movie.year,
            "description": movie.description,
            "ranking": movie.ranking,
            "rating": movie.rating,
            "review": movie.review,
            "image_url": movie.img_url
        }
        movies.append(movie_data)  # list of movies, data of each movie is a dictionary


@app.route("/", methods=['GET'])
def home():
    return render_template("index.html", movies=movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    # receive movie_id param
    movie_id = request.args.get("movie_id")
    selected_movie = db.get_or_404(Movie, movie_id)
    update_form = UpdateForm()
    # Updated The Rating and Description
    if request.method == "POST":
        submitted_form = request.form
        selected_movie.rating = submitted_form["new_rating"]
        selected_movie.description = submitted_form["new_description"]
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", selected_movie=selected_movie, form=update_form)


@app.route("/delete", methods=["GET", "POST"])
def delete():
    movie_id = request.args.get('movie_id')
    selected_movie = db.get_or_404(Movie, movie_id)
    db.session.delete(selected_movie)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/find")
def find():
    movie_id = request.args.get("id")
    print(movie_id)
    if movie_id:
        movie_object = tmdb.Movies(id=movie_id)
        movie_info = movie_object.info()
        new_movie = Movie(
            title=movie_info["title"],
            year=movie_info["release_date"],
            description=movie_info["overview"],
            img_url=f"{TMDB_BASE_IMAGE_URL}/{movie_info['poster_path']}"
        )
        db.session.add(new_movie)
        db.session.commit()
        new_saved = db.get_or_404(Movie, new_movie.id)
        print(new_saved.id)
        return redirect(url_for("edit", movie_id=new_saved.id))


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    search = tmdb.Search()
    add_movie_form = AddMovieForm()
    movie_title = ""
    if request.method == "POST":
        movie_title = request.form["movie_title"]
        # print(movie_title)
        search_response = search.movie(query=movie_title)  # Response for search
        # print(search_response)  # get original_title and release_date
        results_length = len(search_response["results"])
        # results_length passed to the template because jinja does't support len() function
        return render_template("select.html", search_response=search_response, results_length=results_length)

    return render_template("add.html", form=add_movie_form)


if __name__ == '__main__':
    app.run(debug=True)
