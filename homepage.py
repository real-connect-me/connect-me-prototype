# import os
from flask import Flask, request, url_for, render_template, redirect

app = Flask(__name__)
app.config.from_prefixed_env()
# events = os.environ["events"] # list full of dictionaries with event data
start = 0

@app.route("/", methods=["GET", "POST"])
def homepage():
    f = open("events.txt", "r")
    events = []
    for line in f:
        l = line.split()
        events.append({"name":l[0], "place":l[1], "time":l[2]})
    f.close()
    if request.method == "POST":
        f = open("events.txt", "a")
        events.append({"name":request.form["Event Name"], "place":request.form["Event Place"], "time":request.form["Event Time"]})
        f.write(request.form["Event Name"] + " " +  request.form["Event Place"] + " " + request.form["Event Time"])
        f.close()
    return render_template("home.html", evs=events, s=start)

@app.route("/event-create")
def eventform():
    return render_template("eventcreate.html")

@app.route("/right")
def rightify():
    global start
    start += 3
    return redirect("/")

@app.route("/left")
def leftify():
    global start
    if start >= 3:
        start -= 3
    return redirect("/")
