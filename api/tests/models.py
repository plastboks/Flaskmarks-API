# api/tests/models.py

from ..models import User
from ..core.setup import db
from . import BaseTest


class UserTests(BaseTest):

    def _makeOne(self, email, password):
        return User(email=email,
                    password=password)

    def test_constructor(self):
        instance = self._makeOne(email='user1@email.com',
                                 password='1234')

        self.assertEqual(instance.email, 'user1@email.com')
        self.assertTrue(instance.verify_password('1234'))

    def test_by_email(self):
        instance = self._makeOne(email='user2@email.com',
                                 password='1234',
                                 )
        db.session.add(instance)
        q = User.by_email('user2@email.com')
        self.assertEqual(q.email, 'user2@email.com')

    def test_marks(self):
        instance = self._makeOne(email='user2@email.com',
                                 password='1234',
                                 )
        db.session.add(instance)
        q = User.by_email('user2@email.com')
        mark = q.create_mark("bookmark",
                             "test",
                             "http://example.org",
                             "tag1, tag2, tag3")

        self.assertEqual(mark.type, "bookmark")
        self.assertEqual(mark.title, "test")
        self.assertEqual(mark.url, "http://example.org")

        self.assertTrue(q.get_mark_by_id(mark.id))

        marks = q.marks(1) 
        tags = q.all_tags(1)
