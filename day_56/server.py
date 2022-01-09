from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return '<img src="https://media.giphy.com/media/13CoXDiaCcCoyk/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=1)