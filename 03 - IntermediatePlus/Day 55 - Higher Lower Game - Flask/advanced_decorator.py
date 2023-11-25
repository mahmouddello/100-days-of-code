from flask import Flask

app = Flask(__name__)


def make_bold(func):
    def wrapper():
        text = f"<b>{func()}</b>"
        return text

    return wrapper


def make_italic(func):
    def wrapper():
        text = f"<i>{func()}</i>"
        return text

    return wrapper


@app.route("/bye")
@make_bold
@make_italic
def say_bye():
    return "<h1>Bye!</h1>"


if __name__ == "__main__":
    app.run()
