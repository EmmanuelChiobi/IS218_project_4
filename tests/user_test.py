"""This tests the user configuration"""

import logging

from app import db 
from app.db.models import User, Transaction

def test_adding_user(application):
    """This tests the addition of a user"""
    log = logging.getLogger("myApp")
    with application.app_context():
        assert db.session.query(User).count() == 0
        assert db.session.query(Transaction).count == 0
        user = User('bobgale@gmail.com', 'testtest', is_admin = True)
        db.session.add(user)
        user = User.query.filter_by(email='bobgale@gmail.com').first()
        log.info(user)
        assert user.email == 'bobgale@gmail.com'
        # add user.transactions
        user.transactions = [Transaction(1647, "DEBIT"), Transaction(5164, "CREDIT")]
        db.session.commit()
        assert db.session.query(Transaction).count() == 2
        trans1 = Transaction.query.filter_by(amount=7456).first()
        assert trans1.amount == 7456
        db.session.delete(user)
        db.session.delete(trans1)
        db.session.commit()
        assert db.session.query(User).count() == 0
        assert db.session.query(Transaction).count() == 0
