# flaskmarks/models/tag.py

from sqlalchemy import and_, or_, desc
from ..core.setup import db, config
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

class ApiKey(db.Model):
    __tablename__ = 'apikeys'
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    key = db.Column(db.Unicode(256), nullable=False)
    value = db.Column(db.Unicode(512), nullable=False)

    def __init__(self, owner_id, key):
        self.owner_id = owner_id
        self.key = key
        s = Serializer(config['SECRET_KEY'], expires_in = 600)
        self.value = s.dumps({'user': self.id}).decode('utf-8')

    def __repr__(self):
        return '<ApiKey %d>' % (self.id)
