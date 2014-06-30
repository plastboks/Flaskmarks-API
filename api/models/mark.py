# flaskmarks/models/mark.py

from sqlalchemy import and_, or_, desc
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy
from datetime import datetime as dt
from ..core.setup import db, config
from .tag import Tag

ass_tbl = db.Table('marks_tags', db.metadata,
                   db.Column('left_id', db.Integer, db.ForeignKey('marks.id')),
                   db.Column('right_id', db.Integer, db.ForeignKey('tags.id'))
                   )


class Mark(db.Model):
    __tablename__ = 'marks'
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    type = db.Column(db.Unicode(255), nullable=False)
    title = db.Column(db.Unicode(255), nullable=False)
    url = db.Column(db.Unicode(512), nullable=False)
    clicks = db.Column(db.Integer, default=0)
    last_clicked = db.Column(db.DateTime)
    created = db.Column(db.DateTime)
    updated = db.Column(db.DateTime)

    tags = relationship('Tag',
                        secondary=ass_tbl,
                        lazy='joined',
                        backref='marks')

    valid_types = ['bookmark', 'feed', 'youtube']
    valid_feed_types = ['feed', 'youtube']

    def __init__(self, owner_id, created=False):
        self.owner_id = owner_id
        if created:
            self.created = created
        else:
            self.created = dt.utcnow()

    def __repr__(self):
        return '<Mark %r>' % (self.title)
