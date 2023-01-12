from flask import Flask, request, url_for, render_template, redirect
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime

app = Flask(__name__)
app.config.from_pyfile("settings.py")
with app.app_context():
    db = SQLAlchemy(app)
# events = []

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    place= db.Column(db.String, nullable=False)
    time = db.Column(db.String, default=datetime.utcnow)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return self.id

@app.route("/", methods=["GET", "POST"])
def homepage():
    page = request.args.get("page", default = 0, type = int)
    if request.method == "POST":
        event_name = request.form["Event Name"]
        event_place = request.form["Event Place"]
        event_time = request.form["Event Time"]
        new_event = Event(name=event_name, place=event_place, time=event_time)

        try:
            db.session.add(new_event)
            db.session.commit()
        except:
            return "error bruh"
        
        # events.append({"name":request.form["Event Name"], "place":request.form["Event Place"], "time":request.form["Event Time"]})
    events = Event.query.order_by(Event.date_created).all()
    return render_template("home.html", evs=events, page=page)

@app.route("/event-create")
def eventform():
    holdpage = request.args.get("page", default = 0, type = int)
    return render_template("eventcreate.html", p = holdpage)

@app.route("/search", methods=["GET", "POST"])
def searchfor():
    if request.method == "POST":
        searchfor = request.form["Keywords"]
        return [event for event in events if searchfor in event["name"]]
    else:
        return redirect("/")

