from flask import Flask, request, render_template, redirect, session
from flask_session import Session
from cs50 import SQL
# from flask_mail import Mail, Message

app = Flask(__name__)

db = SQL("sqlite:///store.db")

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# app.config["MAIL_DEFAULT_SENDER"] = "bad practice to provide details here without OS"
# app.config["MAIL_PASSWORD"] = "bad practice to provide details here without OS"
# app.config["MAIL_PORT"] = 587
# app.config["MAIL_SERVER"] = "smtp.gmail.com"
# app.config["MAIL_USE_TLS"] = True
# app.config["MAIL_USERNAME"] = "bad practice to provide details here without OS"

# mail = Mail(app)


@app.route("/")
def index():
    books = db.execute("SELECT * FROM books")
    return render_template("index.html", books=books)


@app.route("/cart", methods=["GET", "POST"])
def cart():
    if not session.get("cart"):
        session["cart"] = {}

    # post
    if request.method == "POST":
        id = request.form.get("id")
        if id not in session["cart"]:
            session["cart"][id] = 0
        session["cart"][id] += 1

    # get
    books = db.execute("SELECT * FROM books WHERE id IN (?)",
                       list(session["cart"]))
    return render_template("cart.html", books=books)


@app.route("/buy")
def buy():
    # cart items:

    cart_items = []
    if session["cart"]:
        for item in session["cart"]:
            item_name = db.execute(
                "SELECT title FROM books where id = (?)", item)
            cart_items.append(
                {
                    "id": item,
                    "title": list(item_name)[0]["title"],
                    "qty": session["cart"][item]
                }
            )
        # create message
        # mail_body = "<html><table style='background-color: blue; color: white;'><tr>id</th><th>Title</th><th>qty</th></tr>"
        # for row in cart_items:
        #     item_id = row["id"]
        #     item_title = row["title"]
        #     item_qty = row["qty"]
        #     mail_body += "<tr><td>" + \
        #         str(item_id)+"</td><td>"+str(item_title) + \
        #         "</td><td>"+str(item_qty)+"</td></tr>"
        # mail_body += "</table></html>"

        # message = Message(subject="order placed",
            #   recipients=["dibakash@gmail.com"], html=mail_body)

        # send message
        # mail.send(message)
        # empty cart
        session["cart"] = {}

        return render_template("buy.html", cart_items=cart_items)
    else:
        return render_template("buy.html", cart_items=cart_items)
