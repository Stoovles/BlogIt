import unittest
from blogit.models import User
from blogit import db

class TestUser(unittest.TestCase):

    # def setUp(self) -> None:
    #     pass
    #
    # def tearDown(self) -> None:
    #     pass

    def test_user:
        user = User(username='John Smith', email="test@email.com", password="password")
        db.session.add(user)
        db.session.commit(user)

        self.assertEqual(User.query.first(), user)
        self.assertEqual(User.query.first.username(), user.username)
        self.assertEqual(User.query.first.email(), user.email)
        self.assertEqual(User.query.first.password(), user.password)





