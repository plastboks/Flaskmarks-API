import unittest
import cgi

from webtest import TestApp
from webtest import Upload
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from webob import multidict

from ..core.setup import db


class BaseTestCase(unittest.TestCase):
    """ Base class used for all unittests. This sets up the.
    database and so forth.
    """
    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine('sqlite://')

    def setUp(self):
        db.configure(bind=self.engine)
        self.session = db
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()
        self.session.remove()
