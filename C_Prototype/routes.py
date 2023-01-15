from flask import Blueprint, request, url_for, render_template, redirect
from extentions import db
from models import Event
from forms import SearchForm
from sqlalchemy.sql import text

main = Blueprint('main', __name__)

@main.route("/", methods=["GET", "POST"])
def viewevents():
    page = request.args.get("page", default=0, type=int)
    sform = SearchForm()
    if sform.validate_on_submit():
        return redirect(url_for("main.showresults") + f"?search_query={sform.keywords.data}")
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
        
        # events.mainend({"name":request.form["Event Name"], "place":request.form["Event Place"], "time":request.form["Event Time"]})
    events = Event.query.order_by(Event.date_created).all()
    return render_template("viewevents.html", evs=events, page=page, sform=sform)

@main.route("/event-create")
def eventform():
    holdpage = request.args.get("page", default = 0, type = int)
    return render_template("eventcreate.html", p = holdpage)

@main.route("/results", methods=["GET", "POST"])
def showresults():
    events = Event.query
    keywords = request.args.get("search_query", type=str)
    if keywords:
        events = events.filter(Event.name.like("%" + keywords + "%"))
        events = events.order_by(Event.date_created)
        return render_template("results.html", evs=events)
    else:
        return redirect(url_for("main.viewevents"))
    
