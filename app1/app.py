from email import message
from flask import Flask, render_template, request, redirect
from cs50 import SQL
# from flask_mail import Mail, Message

SPORTS = [
    "MMA",
    "Cricket",
    "Volleyball",
    "Skating",
    "Dodgeball",
    "Karate Kata",
    "Dance",
    "Chess"
]

db = SQL("sqlite:///data.db")

app = Flask(__name__)


# app.config["MAIL_DEFAULT_SENDER"] = "provide email via OS "
# app.config["MAIL_PASSWORD"] = "bad practice to provide pass word here"
# app.config["MAIL_PORT"] = 587
# app.config["MAIL_SERVER"] = "smtp.gmail.com"
# app.config["MAIL_USE_TLS"] = True
# app.config["MAIL_USERNAME"] = "provide username via OS"

# mail = Mail(app)


@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    email = request.form.get("email")
    sport = request.form.get("sport")
    errors = []
    if not name:
        errors.append("name not provided")
    if not email:
        errors.append("email not provided")
    if not sport:
        errors.append("sport not selected")
        return render_template("failure.html", errors=errors)
    if sport not in SPORTS:
        errors.append("wrong sport selected")
        return render_template("failure.html", errors=errors)

    emails = db.execute("SELECT * FROM registrants")
    for mail_id in emails:
        if email == mail_id["email"]:
            return render_template("failure.html", errors=["Email used already"])

    db.execute(
        "INSERT INTO registrants(name, email, sport) VALUES(?,?,?)", name, email, sport)
    # message = Message("You are registered for sports", recipients=[email])

    # mail.send(message)

    return render_template("success.html", name=name, sport=sport)


@app.route("/entries")
def entries():
    return redirect("/registrants")


@app.route("/registrants")
def registrants():
    registrants = db.execute("SELECT * FROM registrants")
    return render_template("registrants.html", registrants=registrants)
