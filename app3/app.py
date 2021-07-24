from flask import Flask, request, redirect, render_template, session, jsonify
from cs50 import SQL

app = Flask(__name__)

db = SQL("sqlite:///shows.db")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search")
def search():
    search = request.args.get("q")
    shows = db.execute(
        "SELECT * FROM shows WHERE title LIKE ?", "%" + search + "%")
    return jsonify(shows)
