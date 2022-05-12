"""This tests the balance calculated for a user"""

import os
from flask_login import FlaskLoginClient
from app import db
from app.db.models import User

def test_user_balance(application):
    application.test_client_class = FlaskLoginClient
    user = User('bobgale@gmail.com', 'newtest', True)
    db.session.add(user)
    db.session.commit()
    assert user.email == 'bobgale@gmail.com'
    assert user.balance == 0.00
    user.balance += 4.20
    assert user.balance == 4.20
    user.balance -= 2.50
    assert user.balance == 1.70