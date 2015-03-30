# flaskmarks/models/tag.py

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from sqlalchemy import and_, or_, desc
from datetime import datetime, timedelta
import bcrypt
from ..core.setup import db, config#, bcrypt
import uuid


class ApiKey(db.Model):
    __tablename__ = 'ApiKey'

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    key = db.Column(db.Unicode(256), nullable=False)
    value = db.Column(db.Unicode(512), nullable=False)
    expires = db.Column(db.DateTime)
    created = db.Column(db.DateTime, default=datetime.utcnow())

    default_expi = 60**3
    unhashed = ""

    def __init__(self, owner_id, key):
        self.owner_id = owner_id
        self.key = key
        self.value = str(uuid.uuid4())
        self.expires = datetime.utcnow() + timedelta(seconds=self.default_expi)
        self.set_unhashed()

    def set_unhashed(self):
        s = Serializer(config['SECRET_KEY'], expires_in = self.default_expi)
        self.unhashed = s.dumps({'uuid' : self.value})
        
    def __repr__(self):
        return '<ApiKey %d>' % (self.id)
