from flask import Flask, render_template, request
import datetime as dt
import git

app = Flask(__name__)


@app.route("/personal_site", methods=["POST"])
def webhook():
    if request.method == "POST":
        repo = git.Repo("https://github.com/jamesslinger/Personal-Site-v2.0.git")
        origin = repo.remotes.origin
        origin.pull()
        return "Updated PA successfully", 200
    else:
        return "Wrong event type", 400


@app.route("/")
def home_page():
    current_year = dt.datetime.now().year
    return render_template("index.html", year=current_year)


@app.route("/projects.html")
def projects():
    current_year = dt.datetime.now().year
    return render_template("projects.html", year=current_year)


if __name__ == "__main__":
    app.run(debug=True)
