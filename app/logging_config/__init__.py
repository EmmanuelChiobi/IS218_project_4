from http.client import responses
import logging
import os
from logging.config import dictConfig

import flask
from flask import request, current_app

from app import config

log_con = flask.Blueprint('log_con', __name__)

@log_con.after_app_request
def after_request_logging(response):
    if request.path == '/favicon.ico':
        return response
    elif request.path.startswith('/static'):
        return response
    elif request.path.startswith('/bootstrap'):
        return response
    