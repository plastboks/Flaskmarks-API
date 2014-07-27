# api/tests/models.py

from ..core.setup import bcrypt
from . import BaseTest


class UserModelTests(BaseTest):

    def _getTargetClass(self):
        from ..models import User
        return User

    def _makeOne(self, email, password, id=False):
        hashed = bcrypt.generate_password_hash(password)
        if id:
            return self._getTargetClass()(id=id,
                                          email=email,
                                          password=hashed)
        return self._getTargetClass()(email=email,
                                      password=hashed,
                                      )

    def test_constructor(self):
        instance = self._makeOne(email='user1@email.com',
                                 password='1234',
                                 )
        self.assertEqual(instance.email, 'user1@email.com')
        self.assertTrue(instance.verify_password('1234'))

    def test_by_email(self):
        instance = self._makeOne(email='user2@email.com',
                                 password='1234',
                                 )
        db.session.add(instance)
        q = self._getTargetClass().by_email('user2@email.com')
        self.assertEqual(q.email, 'user2@email.com')

    def test_by_id(self):
        instance = self._makeOne(email='user3@email.com',
                                 password='1234',
                                 id=1000,
                                 )
        db.session.add(instance)
        q = self._getTargetClass().by_id(1000)
        self.assertEqual(q.email, 'user3@email.com')
