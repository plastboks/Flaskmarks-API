# flaskmarks/models/setting.py

from ..core.setup import db
from datetime import datetime as dt


class Setting(db.Model):
    __tablename__ = 'Setting'

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    name = db.Column(db.Unicode(256), nullable=False)
    json = db.Column(db.Unicode(4096), nullable=False)
    status = db.Column(db.Integer, default=1)
    created = db.Column(db.DateTime)
    updated = db.Column(db.DateTime)

    status_map = {'active': 1, 'inactive': 2}

    def __init__(self, owner_id, name, json):
        self.owner_id = owner_id
        self.created = dt.utcnow()
        self.name = name
        self.json = json

    def update(self, args):
        for key, value in args.iteritems():
            setattr(self, key, value)
        self.updated = dt.utcnow()
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        self.status = self.status_map['inactive']
        self.updated = dt.utcnow()
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return '<Setting %d>' % (self.id)
