from flask import Flask, render_template, request, redirect
from cs50 import SQL
# from flask_mail import Mail, Message

app = Flask(__name__)
# app.config["MAIL_DEFAULT_SENDER"] = "clients.digiattract@gmail.com"
# app.config["MAIL_PASSWORD"] = "no pass here bad practice"
# app.config["MAIL_PORT"] = 587
# app.config["MAIL_SERVER"] = "smtp.gmail.com"
# app.config["MAIL_USE_TLS"] = True
# app.config["MAIL_USERNAME"] = "clients.digiattract@gmail.com"

SPORTS = [
    "MMA",
    "Karate",
    "Soccer",
    "Skating",
    "Cricket",
    "Fencing"
]

db = SQL("sqlite:///data.db")

# mail = Mail(app)


@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("firstName")
    email = request.form.get("email")
    sport = request.form.get("sport")
    if not name:
        return render_template("failure.html", error="Name not provided")
    if not email:
        return render_template("failure.html", error="Email not provided")
    if sport not in SPORTS:
        return render_template("failure.html", error="wrong sports!")

    # save data
    db.execute(
        "INSERT INTO registrants(name, email, sport) VALUES(?, ? ,?)", name, email, sport)

    # send mail
    # message = Message("You are successfully registered", recipients=[email])
    # mail.send(message)

    return render_template("success.html", name=name)


@app.route("/registrants")
def registrants():
    registrants = db.execute("SELECT * FROM registrants")
    return render_template("registrants.html", registrants=registrants)
