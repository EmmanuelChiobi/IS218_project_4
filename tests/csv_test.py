"""This tests the upload of a csv file"""

import os
from flask_login import FlaskLoginClient
from app import db
from app.db.models import User
from app.auth.forms import csv_upload

def test_csv_upload_success(application):
    """This tests if the upload of a transactions csv file was a success"""
    application.test_client_class = FlaskLoginClient
    user = User('bobgale@gmail.com', 'test2', 1)
    db.session.add(user)
    db.session.commit()
    assert user.email == 'bobgale@gmail.com'
    # after applying to db, initialize csv
    root = os.path.dirname(os.path.abspath(__file__))
    csv_file = os.path.join(root, '../uploads/csv_file_output.csv')

    with application.test_client(user = user) as client:
        response = client.get('/transactions/upload')
        assert response.status_code == 200
        form = csv_upload()
        form.file = csv_file
        assert form.validate

def test_csv_upload_denied(application):
    """This tests if the upload of a transactions csv file was a failure"""
    application.test_client_class = FlaskLoginClient
    assert db.session.query(User).count() == 1
    with application.test_client (user = None) as client:
        response = client.get('/transactions/upload')
        assert response.status_code == 302

def test_user_balance(application):
    """This tests the calculation of a user's balance"""
    application.test_client_class = FlaskLoginClient
    user = User('robertgale@gmail.com', 'newtest2', True)
    db.session.add(user)
    db.session.commit()
    assert user.email == 'robertgale@gmail.com'
    assert user.balance == 0.00
    user.balance += 4.25
    assert user.balance == 4.25
    user.balance -= 2.51
    assert user.balance == (4.25 - 2.51)
