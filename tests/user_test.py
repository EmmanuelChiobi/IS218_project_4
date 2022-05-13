"""This tests the user configuration"""

import logging
from app import db
from app.db.models import User, Transaction

def test_adding_user(application):
    """This tests the addition of a user"""
    log = logging.getLogger("myApp")
    with application.app_context():
        assert db.session.query(User).count() == 0
        assert db.session.query(Transaction).count() == 0
        # create a user (record)
        user = User('bobgale@gmail.com', 'newtest', 1)
        # add record
        db.session.add(user)
        # find user by email
        user = User.query.filter_by(email='bobgale@gmail.com').first()
        log.info(user)
        # assert that email is correct
        assert user.email == 'bobgale@gmail.com'
        # insert attributes to related record
        user.transactions = [Transaction(-1647, "DEBIT"), Transaction(5164, "CREDIT")]
        # transactions are saved via commit
        db.session.commit()
        assert db.session.query(Transaction).count() == 2
        trans1 = Transaction.query.filter_by(AMOUNT=-1647).first()
        assert trans1.AMOUNT == -1647
        # change the amount of the first transaction
        trans1.amount = 2569
        # saving the new amount
        db.session.commit()
        trans2 = Transaction.query.filter_by(AMOUNT=5164).first()
        assert trans2.AMOUNT == 5164
        # checking cascade delete
        db.session.delete(user)
        assert db.session.query(User).count() == 0
        assert db.session.query(Transaction).count() == 0
