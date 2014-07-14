# api/core/setup.py

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.bcrypt import Bcrypt
from flask.ext.restful import Resource, Api
from flask.ext.httpauth import HTTPBasicAuth
from flask.ext.sslify import SSLify

from .. import app

app.config.from_object('config')
config = app.config

"""
Debug mode
"""
app.debug = config['DEBUG_MODE']

"""
SSL
"""
sslify = SSLify(app)

"""
Database ORM
"""
db = SQLAlchemy(app)

"""
DB migration
"""
migrate = Migrate(app, db)

"""
Manager
"""
manager = Manager(app)
manager.add_command('db', MigrateCommand)

"""
Bcrypt
"""
bcrypt = Bcrypt(app)

"""
RESTful
"""
api = Api(app, catch_all_404s=True)

"""
Auth
"""
auth = HTTPBasicAuth()
