from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/cv")
def cv_home():
    return render_template("cv/tb.html")


if __name__ == "__main__":
    app.run(debug=1)
