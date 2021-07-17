from flask import Flask, render_template, request, redirect

app = Flask(__name__)

REGISTRANTS = {}

SPORTS = ["cricket", "MMA", "soccer", "skating", "football"]


@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    sport = request.form.get("sport")
    if not name:
        return render_template("failure.html", message="Name not provided")
    if not sport:
        return render_template("failure.html", message="Sport not provided")
    if sport not in SPORTS:
        return render_template("failure.html", message="Incorrect Sports")

    REGISTRANTS[name] = sport

    return render_template("success.html", firstName=name, sport=sport)


@app.route("/registrants")
def registrants():
    return render_template("registrants.html", registrants=REGISTRANTS)
