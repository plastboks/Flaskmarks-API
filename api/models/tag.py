# flaskmarks/models/tag.py

from ..core.setup import db


class Tag(db.Model):
    __tablename__ = 'Tag'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Unicode(255), nullable=False)

    def __init__(self, title):
        self.title = title

    def update(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def check(self, title):
        return self.query.filter(Tag.title == title).first()

    def __repr__(self):
        return '<Tag %r>' % (self.title)
