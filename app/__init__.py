"""A simple flask web app"""
import os

import flask_login
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_cors import CORS
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect

from app.auth import auth
from app.cli import create_database
from app.context_processors import utility_text_processors
from app.db import db, database
from app.db.models import User
from app.error_handlers import error_handlers
from app.logging_config import log_con, LOGGING_CONFIG
from app.simple_pages import simple_pages
from app.transactions import transactions

mail = Mail()
login_manager = flask_login.LoginManager()

def page_not_found(e):
    return render_template("404.html"), 404

def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    if os.environ.get("FLASK_ENV") == "production":
        app.config.from_object("app.config.ProductionConfig")
    elif os.environ.get("FLASK_ENV") == "development":
        app.config.from_object("app.config.DevelopmentConfig")
    elif os.environ.get("FLASK_ENV") == "testing":
        app.config.from_object("app.config.TestingConfig")
    app.secret_key = 'This is an INSECURE secret!! DO NOT use this in production!!'
    app.mail = Mail(app)

    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    app.register_error_handler(404, page_not_found)
    db_dir = "database/db.sqlite"
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.abspath(db_dir)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    # add command function to cli commands
    app.cli.add_command(create_database)

    return app

@login_manager.user_loader
def user_loader(user_id):
    try:
        return User.query.get(int(user_id)) 
    except:
        return None
