# api/models/user.py

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired
from sqlalchemy import or_, and_, desc, asc
from datetime import datetime
from ..core.setup import db, config
from .tag import Tag
from .mark import Mark
from .apikey import ApiKey
from .setting import Setting
import bcrypt


class User(db.Model):
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Integer, default=1)
    email = db.Column(db.Unicode(255), unique=True, nullable=False)
    username = db.Column(db.Unicode(128), unique=True)
    password = db.Column(db.Unicode(255), nullable=False)
    per_page = db.Column(db.SmallInteger, default=20)
    sort_type = db.Column(db.Unicode(255), default=u'clicks')
    created = db.Column(db.DateTime, default=datetime.utcnow())
    last_logged_in = db.Column(db.DateTime)

    marks = db.relationship('Mark', backref='owner', lazy='dynamic')
    apikeys = db.relationship('ApiKey', backref='owner', lazy='joined')
    settings = db.relationship('Setting', backref='owner', lazy='joined')

    smap = {'active': 1, 'inactive': 2}

    def __init__(self, email, password):
        self.email = email
        self.password = bcrypt.hashpw(password, bcrypt.gensalt())

    def update(self, args):
        for key, value in args.iteritems():
            if value:
                setattr(self, key, value)
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        self.status = self.smap['inactive']
        for apikey in self.my_apikeys():
            apikey.delete()
        db.session.add(self)
        db.session.commit()
        return self

    def save(self):
        if not User.by_email(self.email):
            db.session.add(self)
            db.session.commit()
            return self
        return False

    """
    Authentication
    """
    @classmethod
    def by_email(self, email):
        return self.query.filter(and_(User.email == email,
                                      User.status == self.smap['active']))\
                         .first()

    @staticmethod
    def verify_api_key(token):
        s = Serializer(config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None
        except BadSignature:
            return None
        t = ApiKey.query.filter(ApiKey.value == data['uuid']).first()
        if t and t.expires > datetime.utcnow():
            # renew key
            t.renew()
            t.update()
            if (t.owner.status == User.smap['active']):
                return t.owner
        return None

    def verify_password(self, password):
        return bcrypt.hashpw(password, self.password) == self.password

    def is_authenticated(self):
        return True

    def is_active(self):
        return self.status == self.smap['active']

    def is_anonymous(self):
        return True

    def get_id(self):
        return unicode(self.id)

    """
    Marks
    """
    def create_mark(self, type, title, url, tags):
        m = Mark(self.id, type, title, url)
        if tags:
            m.update_tags(tags)
        db.session.add(m)
        db.session.commit()
        return m

    def my_marks(self):
        return Mark.query.filter(and_(Mark.owner_id == self.id,
                                      Mark.status == self.smap['active']))

    def get_mark_by_id(self, id):
        mark = self.my_marks().filter(and_(Mark.id == id,
                                           Mark.status == self.smap['active']))\
                              .first()
        if mark:
            mark.increment_clicks()
            return mark
        return None

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
    Settings
    """
    def create_setting(self, name, client, json):
        setting = Setting(self.id, name, json)
        if client:
            setting.client = client
        db.session.add(setting)
        db.session.commit()
        return setting

    def my_settings(self):
        return Setting.query.filter(Setting.owner_id == self.id)

    def settings(self, page):
        return self.my_settings().paginate(page, self.per_page, False)

    def get_setting_by_name(self, name):
        return self.my_settings().filter(Setting.name == name).first()

    """
    Tags
    """
    def my_tags(self):
        return Tag.query.filter(Tag.Mark.any(owner_id=self.id))

    def all_tags(self, page):
        return self.my_tags().paginate(page, self.per_page, False)

    """
    Generic
    """
    def json_pager(self, obj):
        return {'page': obj.page,
                'pages': obj.pages,
                'next_num': obj.next_num if obj.has_next else -1,
                'prev_num': obj.prev_num if obj.has_prev else -1,
                'total': obj.total}

    def __repr__(self):
        return '<User %r>' % (self.username)
