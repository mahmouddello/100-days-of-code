from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

books = []

# create the extension
db = SQLAlchemy()

# create the app
app = Flask(__name__)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

# initialize the app with the extension
db.init_app(app)


# CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


with app.app_context():
    db.create_all()
    all_books = Book.query.all()
    for book_data in all_books:
        data = {
            "id": book_data.id,
            "title": book_data.title,
            "author": book_data.author,
            "rating": book_data.rating
        }
        books.append(data)


@app.route("/")
def index():
    return render_template("index.html", books=books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        form = request.form
        book = Book(title=form["book_name"], author=form["book_author"], rating=form["book_rating"])
        db.session.add(book)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        book_id = request.form["id"]
        print(book_id == "")
        book_to_update = db.get_or_404(Book, book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('index'))
    book_id = request.args.get('book_id')
    book_selected = db.get_or_404(Book, book_id)
    return render_template("edit.html", book=book_selected)


if __name__ == "__main__":
    app.run()
