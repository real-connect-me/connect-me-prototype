from flask import Blueprint, request, url_for, render_template, redirect
from extentions import db
from models import Event
from forms import SearchForm

main = Blueprint('main', __name__)

@main.route("/", methods=["GET", "POST"])
def homepage():
    page = request.args.get("page", default = 0, type = int)
    sform = SearchForm()
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
    events = Event.query.order_by(Event.date_created).all()
    return render_template("viewevents.html", evs=events, page=page, sform=sform)

@main.route("/event-create")
def eventform():
    holdpage = request.args.get("page", default = 0, type = int)
    return render_template("eventcreate.html", p = holdpage)

@main.route("/search", methods=["GET", "POST"])
def searchfor():
    events = Event.query.order_by(Event.date_created).all()
    if request.method == "POST":
        return "haven't added functionality"
        # searchfor = request.form["Keywords"]
        # return [event for event in events if searchfor in event["name"]]
    else:
        return redirect("/")
