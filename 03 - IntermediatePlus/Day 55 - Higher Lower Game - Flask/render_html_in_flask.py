from flask import Flask

app = Flask(__name__)


@app.route("/")
def return_html():
    return "<h1 style='text-align: center'>Html from return statement</h1>"""


if __name__ == "__main__":
    app.run(debug=True)
