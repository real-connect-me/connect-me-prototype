from flask import Flask
from .extentions import db
from .commands import create_tables
from .routes import main

app = Flask(__name__)
app.config.from_pyfile("settings.py")
db.init_app(app)
app.register_blueprint(main)
app.cli.add_command(create_tables)


