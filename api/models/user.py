# api/models/user.py

from sqlalchemy import or_, desc, asc, func
from sqlalchemy.orm import aliased
from datetime import datetime
from ..core.setup import db, config, bcrypt
from .tag import Tag
from .mark import Mark


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Unicode(255), unique=True, nullable=False)
    username = db.Column(db.Unicode(128), unique=True)
    password = db.Column(db.Unicode(255), nullable=False)
    per_page = db.Column(db.SmallInteger, default=10)
    sort_type = db.Column(db.Unicode(255), default=u'clicks')
    created = db.Column(db.DateTime, default=datetime.utcnow())
    last_logged_in = db.Column(db.DateTime)

    marks = db.relationship('Mark', backref='owner', lazy='dynamic')

    def __init__(self, email=False, password=False):
        if email:
            self.email = email
        if password:
            self.password = bcrypt.generate_password_hash(password)

    """
    Authentication
    """
    @classmethod
    def by_email(self, email):
        return self.query.filter(User.email == email).first()

    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

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
        return Mark.query.filter(Mark.owner_id == self.id)

    def my_tags(self):
        return Tag.query.filter(Tag.marks.any(owner_id=self.id))

    def all_marks(self):
        return self.my_marks().all()

    def marks(self, page, sort=False):
        base = self.my_marks()

        if sort and sort in ['clicks', 'dateasc', 'datedesc']:
            self.sort_type = sort

        if self.sort_type == u'clicks':
            base = base.order_by(desc(Mark.clicks))\
                       .order_by(desc(Mark.created))
        if self.sort_type == u'dateasc':
            base = base.order_by(asc(Mark.created))
        if self.sort_type == u'datedesc':
            base = base.order_by(desc(Mark.created))
        return base.paginate(page, self.per_page, False)

    def json_pager(self, obj):
        return {'page': obj.page,
                'pages': obj.pages,
                'next_num': obj.next_num,
                'prev_num': obj.prev_num,
                'total': obj.total}

    def recent_marks(self, page, type):
        if type == 'added':
            base = self.my_marks().order_by(desc(Mark.created))
            return base.paginate(page, self.per_page, False)
        if type == 'clicked':
            base = self.my_marks().filter(Mark.clicks > 0)\
                                  .order_by(desc(Mark.last_clicked))
            return base.paginate(page, self.per_page, False)
        return False

    def get_mark_by_id(self, id):
        return self.my_marks().filter(Mark.id == id).first()

    def get_mark_type_count(self, type):
        return self.my_marks().filter(Mark.type == type).count()

    def mark_last_created(self):
        return self.my_marks().order_by(desc(Mark.created)).first()

    def q_marks_by_tag(self, tag, page):
        return self.my_marks().filter(Mark.tags.any(title=tag))\
                              .paginate(page, self.per_page, False)

    def q_marks_by_string(self, page, string, marktype):
        string = "%"+string+"%"
        base = self.my_marks().filter(or_(Mark.title.like(string),
                                          Mark.url.like(string)))
        return base.order_by(desc(Mark.clicks))\
                   .paginate(page, self.per_page, False)

    def q_marks_by_url(self, string):
        return self.my_marks().filter(Mark.url == string).first()

    def all_tags(self):
        return self.my_tags().all()

    def tags_by_click(self, page):
        return self.my_tags().order_by(Tag.marks.any(Mark.clicks))\
                             .paginate(page, self.per_page, False)

    def save(self):
        if not User.by_email(self.email):
            db.session.add(self)
            db.session.commit()
            return self
        return False

    def __repr__(self):
        return '<User %r>' % (self.username)
