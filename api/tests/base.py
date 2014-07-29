# api/tests/base.py

from flask.ext.testing import TestCase
import tempfile

from .. import app
from ..core.setup import db

class BaseTest(TestCase):

    SQLALCHEMY_DATABASE_URI = tempfile.mkstemp()
    TESTING = True

    def create_app(self):
        self.db = db
        # pass in test configuration
        return app

    def setUp(self):
        self.db.create_all()

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()
