import os
import click
from flask.cli import with_appcontext
from app.db import db

@click.command(name='create-log')
@with_appcontext
def create_logs():
    # set the name of the apps log folder to logs
    root = os.path.dirname(os.path.abspath(__file__))
    # make a directory if it doesn't exist
    logdir = os.path.join(root, '../logs')
    if not os.path.exist(logdir):
        os.mkdir(logdir)

@click.command(name='create-db')
@with_appcontext
def create_database():
    root = os.path.dirname(os.path.abspath(__file__))
    # make a directory if it doesn't exist
    
    db.create_all()