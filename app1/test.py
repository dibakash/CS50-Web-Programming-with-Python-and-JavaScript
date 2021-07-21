from cs50 import SQL

db = SQL("sqlite:///data.db")

all = db.execute("SELECT email FROM registrants")

for rows in all:
    print(rows)
