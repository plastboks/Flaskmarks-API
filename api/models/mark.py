# flaskmarks/models/mark.py

from sqlalchemy.orm import relationship
from datetime import datetime as dt
from ..core.setup import db
from .tag import Tag

ass_tbl = db.Table('MarkTag', db.metadata,
                   db.Column('left_id', db.Integer, db.ForeignKey('Mark.id')),
                   db.Column('right_id', db.Integer, db.ForeignKey('Tag.id'))
                   )


class Mark(db.Model):
    __tablename__ = 'Mark'

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    status = db.Column(db.Integer, default=1)
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
                        backref='Mark')

    status_map = {'active': 1, 'inactive': 2}

    valid_types = ['bookmark', 'feed']

    def __init__(self, owner_id, type, title, url, created=False):
        self.owner_id = owner_id
        self.type = type
        self.title = title
        self.url = url

        if created:
            self.created = created
        else:
            self.created = dt.utcnow()

    def update(self, args):
        for key, value in args.iteritems():
            if value and key == 'tags':
                self.update_tags(value)
            elif value:
                setattr(self, key, value)
        self.updated = dt.utcnow()
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        self.status = self.status_map['inactive']
        db.session.add(self)
        db.session.commit()

    def update_tags(self, string):
        tagslist = []
        tagsparse = string.strip().replace(',', ' ').split(' ')
        for t in tagsparse:
            tag = Tag.check(t.lower())
            if not tag:
                tag = Tag(t.lower())
                db.session.add(tag)
            tagslist.append(tag)
        self.tags = tagslist

    def increment_clicks(self):
        self.clicks += 1
        self.last_clicked = dt.utcnow()
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return '<Mark %r>' % (self.title)
