"""This tests the clicks"""

import os
from click.testing import CliRunner
from app import create_database, create_logs

runner = CliRunner()

def test_create_logs():
    """This tests the creation of the logs"""
    response = runner.invoke(create_logs)
    assert response.exit_code == 0
    root = os.path.dirname(os.path.abspath(__file__))
    logdir = os.path.join(root, '../logs')
    assert os.path.exists(logdir) is True

def test_create_database():
    """This tests the creation of the database"""
    response = runner.invoke(create_database)
    assert response.exit_code == 0
    root = os.path.dirname(os.path.abspath(__file__))
    # set the name of the apps log folder to logs
    dbdir = os.path.join(root, '../database')
    # make a directory if it doesn't exist
    assert os.path.exists(dbdir) is True
