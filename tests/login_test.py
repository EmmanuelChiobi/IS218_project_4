"""This tests the login and registration of a user"""

import logging
from app.auth.forms import login_form, register_form

def login_test(application):
    """This tests the login"""
    log = logging.getLogger("myApp")
    log.info("User Login Test")
    with application.test_request_context():
        form = login_form()
        form.email.data = "bobgale@gmail.com"
        form.password.data = "newtest"
        assert form.validate

def registration_test(application):
    """This tests the registration"""
    log = logging.getLogger("myApp")
    log.info("User Register Test")
    with application.test_request_context():
        form = register_form()
        form.email.data = "bobgale@gmail.com"
        form.password.data = "newtest"
        form.confirm.data = "newtest"
        assert form.validate
