# import os
from flask import Flask, request, url_for, render_template, redirect

app = Flask(__name__)
# app.config.from_prefixed_env()
# events = os.environ["events"] # list full of dictionaries with event data
events = []

@app.route("/", methods=["GET", "POST"])
def homepage():
    page = request.args.get("page", default = 0, type = int)
    if request.method == "POST":
        events.append({"name":request.form["Event Name"], "place":request.form["Event Place"], "time":request.form["Event Time"]})
    return render_template("home.html", evs=events, page=page)

@app.route("/event-create")
def eventform():
    holdpage = request.args.get("page", default = 0, type = int)
    return render_template("eventcreate.html", p = holdpage)

@app.route("/search", methods=["GET", "POST"])
def searchfor():
    if request.method == "POST":
        searchfor = request.form["Keywords"]
        return "hi"
    else:
        return redirect("/")

