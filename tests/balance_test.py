"""This tests the balance calculated for a user"""

import os
from flask_login import FlaskLoginClient
from app import db
from app.db.models import User