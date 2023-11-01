from flask import Flask, render_template
import datetime as dt

app = Flask(__name__)


@app.route("/")
def home_page():
    current_year = dt.datetime.now().year
    return render_template("index.html", year=current_year)


@app.route("/projects")
def projects():
    current_year = dt.datetime.now().year
    return render_template("projects.html", year=current_year)


if __name__ == "__main__":
    app.run()
