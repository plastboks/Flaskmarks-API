# api/tests/base.py

from flask import Flask
from flask.ext.testing import TestCase
import tempfile

from .. import app
from ..core.setup import db

class BaseTest(TestCase):

    SQLALCHEMY_DATABASE_URI = tempfile.mkstemp()
    TESTING = True

    def create_app(self):
        return Flask(self)

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
