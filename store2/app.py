from flask import Flask, render_template, redirect, request, session
from flask_session import Session
from cs50 import SQL


app = Flask(__name__)
db = SQL("sqlite:///store.db")


app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)


@app.route("/")
def index():
    books = db.execute("SELECT * FROM books")
    return render_template("index.html", books=books)


@app.route("/cart", methods=["GET", "POST"])
def cart():
    # create cart
    if not session.get("cart"):
        session["cart"] = {}

    # POST
    if request.method == "POST":
        id = request.form.get("id")
        if id not in session["cart"]:
            session["cart"][id] = 0
        session["cart"][id] += 1

    # GET
    books = db.execute(
        "SELECT * FROM books WHERE id IN (?)", list(session["cart"]))
    return render_template("cart.html", books=books)
