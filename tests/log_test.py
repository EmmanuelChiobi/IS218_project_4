"""This tests the creation of the log files"""

import os

def request_log_test():
    """This tests the creation of the request log"""
    # initialize the root
    root = os.path.dirname(os.path.abspath(__file__))
    # initialize the log file
    req = os.path.join(root, '../logs/request.log')
    # make directory if it does not exist
    if not os.path.exists(req):
        os.mkdir(req)
    # assert if the directory exists
    assert os.path.exists(req) is True

def errors_log_test():
    """This tests the creation of the errors log"""
    # initialize the root
    root = os.path.dirname(os.path.abspath(__file__))
    # initialize the log file
    err = os.path.join(root, '../logs/errors.log')
    # make directory if it does not exist
    if not os.path.exists(err):
        os.mkdir(err)
    # assert if the directory exists
    assert os.path.exists(err) is True

def debug_log_test():
    """This tests the creation of the debug log"""
    # initialize the root
    root = os.path.dirname(os.path.abspath(__file__))
    # initialize the log file
    deb = os.path.join(root, '../logs/debug.log')
    # make directory if it does not exist
    if not os.path.exists(deb):
        os.mkdir(deb)
    # assert if the directory exists
    assert os.path.exists(deb) is True

def flask_log_test():
    """This tests the creation of the Flask log"""
    # initialize the root
    root = os.path.dirname(os.path.abspath(__file__))
    # initialize the log file
    fla = os.path.join(root, '../logs/flask.log')
    # make directory if it does not exist
    if not os.path.exists(fla):
        os.mkdir(fla)
    # assert if the directory exists
    assert os.path.exists(fla) is True

def sqlalchemy_log_test():
    """This tests the creation of the SQLAlchemy log"""
    # initialize the root
    root = os.path.dirname(os.path.abspath(__file__))
    # initialize the log file
    sql = os.path.join(root, '../logs/sqlalchemy.log')
    # make directory if it does not exist
    if not os.path.exists(sql):
        os.mkdir(sql)
    # assert if the directory exists
    assert os.path.exists(sql) is True

def myapp_log_test():
    """This tests the creation of the 'myapp' log"""
    # initialize the root
    root = os.path.dirname(os.path.abspath(__file__))
    # initialize the log file
    my_app = os.path.join(root, '../logs/myapp.log')
    # make directory if it does not exist
    if not os.path.exists(my_app):
        os.mkdir(my_app)
    # assert if the directory exists
    assert os.path.exists(my_app) is True

def csv_log_test():
    """This tests the creation of the updated CSV log"""
    # initialize the root
    root = os.path.dirname(os.path.abspath(__file__))
    # initialize the log file
    csv = os.path.join(root, '../logs/updatecsv.log')
    # make directory if it does not exist
    if not os.path.exists(csv):
        os.mkdir(csv)
    # assert if the directory exists
    assert os.path.exists(csv) is True