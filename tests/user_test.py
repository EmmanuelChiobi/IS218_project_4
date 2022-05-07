"""This tests the user configuration"""

import logging

from app import db 
from app.db.models import User

def test_adding_user(application):
    log = logging.getLogger("myApp")
    with application.app_context():
        assert db.session.query(User).count() == 0
        user = User('bobgale@gmail.com', 'testtest', is_admin = True)
        db.session.add(user)
        user = User.query.filter_by(email='bobgale@gmail.com').first()
        log.info(user)
        assert user.email == 'bobgale@gmail.com'
        # add user.transactions
        