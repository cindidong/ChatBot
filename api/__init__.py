from flask import Flask
from flask_migrate import Migrate
from api.database import db
import os
from .config import config

migrate = Migrate()

def create_app(config_mode):
    app = Flask(__name__)
    app.config.from_object(config[config_mode])
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DEVELOPMENT_DATABASE_URL")

    db.init_app(app)
    migrate.init_app(app, db)

    return app