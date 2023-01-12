from flask import Flask
import os, sys; sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from extentions import db
from commands import create_tables
from routes import main

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("settings.py")
    db.init_app(app)
    app.register_blueprint(main)
    app.cli.add_command(create_tables)
    return app


