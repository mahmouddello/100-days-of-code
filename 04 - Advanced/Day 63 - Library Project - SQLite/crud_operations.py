from flask import Flask
from flask_sqlalchemy import SQLAlchemy

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


# In addition to these things,
# the most crucial thing to figure out when working with any new database technology is how to CRUD data records.
#
# Create
#
# Read
#
# Update
#
# Delete
def read_all():
    """To read all the records we first need to create a "query" to select things from the database.
    When we execute a query during a database session we get back the rows in the database (a Result object).
    We then use scalars() to get the individual elements rather than entire rows."""
    print("-------- READ ALL -------- ")
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    for book in all_books:
        print(book)
    print("X" * 25)


def read_single_by_query():
    """Read A Particular Record By Query.
     To get a single element we can use scalar() instead of scalars()."""
    print("-------- READ BY QUERY -------- ")
    result = db.session.execute(db.select(Book).where(Book.title == "Interstellar")).scalar()
    print(result)
    print("X" * 25)


def update_record():
    print("-------- UPDATE BY QUERY -------- ")
    book_to_update = db.session.execute(db.select(Book).where(Book.title == "Interstellar")).scalar()
    book_to_update.title = "Interstellar2"
    print("Let's say changes, but we are not committing to the database")
    read_all()


#
# Update A Record By PRIMARY KEY
def update_by_pk():
    print("UPDATE BY PRIMARY KEY, COMMITTING THE CHANGES TO THE DB")
    book_id = 1
    book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    # or book_to_update = db.get_or_404(Book, book_id)
    book_to_update.title = "Harry Potter and the Goblet of Fire"
    db.session.commit()


# Flask-SQLAlchemy also has some handy extra query methods like get_or_404() that we can use. Since Flask-SQLAlchemy
# version 3.0 the previous q

def delete_record():
    # Delete A Particular Record By PRIMARY KEY
    book_id = 1
    book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    # or book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
#
# You can also delete by querying
# for a particular value e.g.by title or one of the other properties.Again, the get_or_404() method is quite handy.


with app.app_context():
    read_all()
    read_single_by_query()
    # update_record()
    # update_by_pk()
    # read_all()
    # delete_record()
    # read_all()
