# api/models/user.py

from sqlalchemy import or_, and_, desc, asc, func
from sqlalchemy.orm import aliased
from datetime import datetime
from ..core.setup import db, config#, bcrypt
from .tag import Tag
from .mark import Mark
from .apikey import ApiKey
import bcrypt


class User(db.Model):
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True)
    active = db.Column(db.Integer, default=1)
    email = db.Column(db.Unicode(255), unique=True, nullable=False)
    username = db.Column(db.Unicode(128), unique=True)
    password = db.Column(db.Unicode(255), nullable=False)
    per_page = db.Column(db.SmallInteger, default=10)
    sort_type = db.Column(db.Unicode(255), default=u'clicks')
    created = db.Column(db.DateTime, default=datetime.utcnow())
    last_logged_in = db.Column(db.DateTime)

    marks = db.relationship('Mark', backref='owner', lazy='dynamic')
    apikeys = db.relationship('ApiKey', backref='owner', lazy='joined')

    master_key = ""

    def __init__(self, email=False, password=False):
        if email:
            self.email = email
        if password:
            self.password = bcrypt.hashpw(password, bcrypt.gensalt())

    """
    Authentication
    """
    @classmethod
    def by_email(self, email):
        return self.query.filter(and_(User.email == email,
                                      User.active == 1)).first()

    @staticmethod
    def verify_api_key(token):
        hashed = bcrypt.hashpw(token, config['APIKEY_SALT'])
        t = ApiKey.query.filter(ApiKey.value == hashed).first()
        if t and t.expires > datetime.utcnow():
            return t.owner
        return None

    def verify_password(self, password):
        return bcrypt.hashpw(password, self.password) == self.password

    def is_authenticated(self):
        return True

    def is_active(self):
        return self.active == 1

    def is_anonymous(self):
        return True

    def get_id(self):
        return unicode(self.id)

    """
    Marks
    """
    def create_mark(self, type, title, url, tags):
        m = Mark(self.id)
        m.type = type
        m.title = title
        m.url = url
        # Tags
        if tags:
            m.update_tags(tags)
        db.session.add(m)
        db.session.commit()
        return m

    def my_marks(self):
        return Mark.query.filter(and_(Mark.owner_id == self.id,
                                      Mark.active == 1))

    def get_mark_by_id(self, id):
        mark = self.my_marks().filter(and_(Mark.id == id,
                                           Mark.active == 1)).first()
        if mark:
            mark.increment_clicks()
            return mark

    def q_marks_by_url(self, string):
        return self.my_marks().filter(Mark.url == string).first()

    def marks(self, page, q=False, type=False, tag=False, sort=False):
        base = self.my_marks()

        if sort and sort in ['clicks', 'dateasc', 'datedesc', 'last_clicked']:
            self.sort_type = sort
        if type and type in Mark.valid_types:
            base = base.filter(Mark.type == type)
        if q:
            q = "%"+q+"%"
            base = base.filter(or_(Mark.title.like(q),
                                   Mark.url.like(q)))
        if tag:
            base = base.filter(Mark.tags.any(title=tag))

        if self.sort_type == u'last_clicked':
            base = self.my_marks().filter(Mark.clicks > 0)\
                                  .order_by(desc(Mark.last_clicked))
        if self.sort_type == u'clicks':
            base = base.order_by(desc(Mark.clicks))\
                       .order_by(desc(Mark.created))
        if self.sort_type == u'dateasc':
            base = base.order_by(asc(Mark.created))
        if self.sort_type == u'datedesc':
            base = base.order_by(desc(Mark.created))
        return base.paginate(page, self.per_page, False)

    """
    Tokens / ApiKeys
    """
    def create_apikey(self, title):
        ak = ApiKey(self.id, title)
        db.session.add(ak)
        db.session.commit()
        return ak

    def my_apikeys(self):
        return ApiKey.query.filter(ApiKey.owner_id == self.id)

    def tokens(self, page):
        return self.my_apikeys().paginate(page, self.per_page, False)

    def get_token_by_key(self, key):
        return self.my_apikeys().filter(ApiKey.key == key).first()

    """
    Tags
    """
    def my_tags(self):
        return Tag.query.filter(Tag.Mark.any(owner_id=self.id))

    def all_tags(self, page):
        return self.my_tags().paginate(page, self.per_page, False)

    """
    Generics
    """
    def json_pager(self, obj):
        return {'page': obj.page,
                'pages': obj.pages,
                'next_num': obj.next_num if obj.has_next else False,
                'prev_num': obj.prev_num if obj.has_prev else False,
                'total': obj.total}

    def save(self):
        if not User.by_email(self.email):
            db.session.add(self)
            db.session.commit()
            return self
        return False

    def __repr__(self):
        return '<User %r>' % (self.username)
