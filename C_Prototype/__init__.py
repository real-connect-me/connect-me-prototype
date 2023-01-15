from flask import Flask
import os, sys; sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from extentions import db
from routes import main
from models import Event

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("settings.py")
    db.init_app(app)
    app.register_blueprint(main)
    with app.app_context():
        db.create_all()
    return app


