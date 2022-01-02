# new version: https://flask.palletsprojects.com/en/2.0.x/quickstart/
#
# $env:FLASK_APP = "hello"
# flask run
#
from flask import Flask

app = Flask(__name__)


# print(__name__)

@app.route("/")
def hello_world():
    return "<p>‘Same Same, But Different’: The Origins of Thailand's Tourist Catchphrase</p>"

@app.route("/bye")
def say_bye():
    return "Bye"

if __name__ == "__main__":
    app.run()
#
