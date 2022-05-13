"""This tests the access to the dashboard page"""

from flask_login import FlaskLoginClient
from app import db
from app.db.models import User

def non_admin_test(application):
    """This test the non-admin users' access to the dashboard page"""
    application.test_client_class = FlaskLoginClient
    with application.test_client(user = None) as client:
        response = client.get('/dashboard')
        assert response.status_code == 302

def admin_test(application):
    """This tests the admin users' access to the dashboard page"""
    application.test_client_class = FlaskLoginClient
    user = User('bobgale@gmail.com', 'newtest', True)
    db.session.add(user)
    db.session.commit()
    assert user.email == 'bobgale@gmail.com'
    with application.test_client(user = user) as client:
        response = client.get('/dashboard')
        assert b'/bobgale@gmail.com' in response.data
        assert response.status_code == 302
        