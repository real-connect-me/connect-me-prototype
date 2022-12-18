# import os
from flask import Flask, request, url_for, render_template, redirect

app = Flask(__name__)
app.config.from_prefixed_env()
# events = os.environ["events"] # list full of dictionaries with event data
events = []
start = 0

@app.route("/", methods=["GET", "POST"])
def homepage():
    if request.method == "POST":
        events.append({"name":request.form["Event Name"], "place":request.form["Event Place"], "time":request.form["Event Time"]})
    return render_template("home.html", evs=events, s=start)

@app.route("/event-create")
def eventform():
    return render_template("eventcreate.html")

