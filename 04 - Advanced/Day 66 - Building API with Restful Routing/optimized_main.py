import random
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

## Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)

TopSecretApiKey = "DeleteMe"


## Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        # Method 1.
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            if column.name == "id":
                pass
            else:
                dictionary[column.name] = getattr(self, column.name)
        return dictionary

        # # Method 2. Alternatively use Dictionary Comprehension to do the same thing.
        # return {column.name: getattr(self, column.name) for column in self.__table__.columns}


def make_bool(val: int) -> bool:
    """
        Takes in a numeric value and converts to boolean

        :param val: Expecting number
        :return: Boolean
        """
    return bool(int(val))


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


## HTTP GET - Read Record

@app.route("/random-cafe")
def get_random_cafe():
    """Returns a Random cafe response from the api call."""
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all")
def get_all():
    """Get all cafes returned from the api, sort them in a list"""
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    lst = [cafe.to_dict() for cafe in all_cafes]  # list comprehension
    return jsonify(cafes=lst)


# HTTP GET, SEARCH FOR A RECORD

@app.route("/search")
def search():
    """Search for all cafes in the location passed as parameter query, expects 'loc' parameter in the request."""
    error_log = {
        "Not Found": "Sorry, we don't have a cafe at this location."
    }
    location = request.args.get("loc")
    result = db.session.execute(db.select(Cafe).where(Cafe.location == location))
    located_cafes = result.scalars().all()
    if located_cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in located_cafes])
    else:
        return jsonify(error=error_log)


## HTTP POST - Create Record

@app.route("/add", methods=["POST"])
def add_cafe():
    form = request.form
    new_cafe = Cafe(
        name=form["name"],
        map_url=form["map_url"],
        img_url=form["img_url"],
        location=form["location"],
        seats=form["seats"],
        has_toilet=make_bool(form["has_toilet"]),
        has_wifi=make_bool(form["has_wifi"]),
        has_sockets=make_bool(form["has_sockets"]),
        can_take_calls=make_bool(form["can_take_calls"]),
        coffee_price=form["coffee_price"]
    )
    db.session.add(new_cafe)
    db.session.commit()
    check_if_added = db.get_or_404(Cafe, new_cafe.id)
    if check_if_added:
        return jsonify(response={
            "success": "Successfully added a new cafe."
        })
    else:
        return jsonify(error={
            "error": "Something went wrong."
        })


## HTTP PUT/PATCH - Update Record

@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_cafe_price(cafe_id):
    new_price = request.args.get("new_price")
    select_cafe = db.get_or_404(Cafe, cafe_id)  # select cafe by id
    if select_cafe:
        select_cafe.coffee_price = "£" + new_price
        db.session.commit()
        return jsonify(response={
            "success": f"Successfully updated the coffe price with cafe id of {select_cafe.id}"
        })
    else:
        return jsonify(error={
            "Not Found": "Sorry a cafe with that id was not found in the database"
        })


## HTTP DELETE - Delete Record

@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    """
    Deletes a Cafe from the database. Fetches the id of the cafe from url, selects the cafe and checks for the api_key.
    api_key is handled as query parameter.
    Parameters
    ----------
    cafe_id: int

    -------

    """
    api_key = request.args.get("api_key")
    selected_cafe = db.get_or_404(Cafe, cafe_id)
    if selected_cafe:
        if api_key.__eq__(TopSecretApiKey):
            db.session.delete(selected_cafe)
            db.session.commit()
            return jsonify(success=f"Successfully deleted cafe with id of {selected_cafe.id}")
        else:
            return jsonify(error="Sorry, that's not allowed. Make sure you have the correct api_key.")
    else:
        return jsonify(error={
            "Not Found": f"Sorry, a cafe with id of {selected_cafe.id} was not found in our database"
        })


if __name__ == '__main__':
    app.run(debug=True)
