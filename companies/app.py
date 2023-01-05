from flask import Flask, render_template, request , redirect
from cs50 import SQL

app = Flask(__name__)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

db = SQL("sqlite:///companies.db")



@app.route("/")
def companies():
        companies = db.execute("SELECT * FROM companies")
        return render_template("index.html", companies = companies)


           
        




