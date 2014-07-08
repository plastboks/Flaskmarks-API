# flaskmarks/models/tag.py

from sqlalchemy import and_, or_, desc
from ..core.setup import db, config


class ApiKey(db.Model):
    __tablename__ = 'apikeys'
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    app = db.Column(db.Unicode(256), nullable=False)
    value = db.Column(db.Unicode(512), nullable=False)

    def __init__(self, app, value):
        self.app = app
        self.title = value

    def __repr__(self):
        return '<ApiKey %d>' % (self.id)
