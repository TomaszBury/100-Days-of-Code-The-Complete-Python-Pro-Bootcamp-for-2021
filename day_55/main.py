# new version: https://flask.palletsprojects.com/en/2.0.x/quickstart/
#
# $env:FLASK_APP = "hello"
# flask run
#
from flask import Flask

app = Flask(__name__)

# "<p style='text-align: center'>‘Same Same, But Different’: " \
#            "The Origins of Thailand's Tourist Catchphrase</p> " \

# '<div style="width:480px"><iframe allow="fullscreen" frameBorder="0" height="278" ' \
#            'src="https://giphy.com/embed/E4Nu9zTcyYiACo8ifL/video" width="480"></iframe></div>'

# print(__name__)

@app.route("/")
def hello_world():
    return '<img src="https://media.giphy.com/media/13CoXDiaCcCoyk/giphy.gif">'


@app.route("/bye")
def say_bye():
    return "Bye___Tests"


@app.route("/username/<name>")
def greet(name):
    return f"Hello there {name}!"

@app.route("/add/<int:karmba>")
def add(karmba):
    sum = 0
    if karmba != 0:
        sum = 420
    else:
        sum = 69
    return f"Karamba: {sum}"


if __name__ == "__main__":
    app.run(debug=1)
#
