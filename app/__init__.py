import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from config import Config

db = SQLAlchemy()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Checking if the instance folder exists
    if not os.path.exists("instance"):
        os.makedirs("instance")  # Creating the instance folder

    # Creating a database
    if not os.path.exists("instance/tasks.db"):
        open("instance/tasks.db", "w").close()  # Creating an empty DATABASE file

    db.init_app(app)
    csrf.init_app(app)

    from app.views import main
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()  # Creating tables if there are none

    return app
