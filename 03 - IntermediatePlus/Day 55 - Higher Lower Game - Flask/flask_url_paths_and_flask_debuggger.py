from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def index_page():
    return "Index"


@app.route("/bye")
def say_bye():
    return "Bye User"


# You can add variable sections to a URL by marking sections with <variable_name>. Your function then receives the
# <variable_name> as a keyword argument. Optionally,
# you can use a converter to specify the type of the argument like <converter:variable_name>.
# Check documentation for more information
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules
@app.route("/username/<name>")
def show_user_profile(name):
    """
    Fetching the <name> variable which the user has typed in the url, and
    preparing a greeting message with the value of the name variable.
    The routing would be something like http://localhost/username/<name>
    Flask will turn anything inside <> into a variable .
    """
    return f"Hello there! {name}"


if __name__ == "__main__":
    # "If we turn the debug mode to true, we got a auto-reload,
    # "without needing to restart the server every time"

    app.run(debug=True)
