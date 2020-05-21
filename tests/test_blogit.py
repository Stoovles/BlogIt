import unittest
from blogit.models import User, Post
from blogit import create_test_app, db

class appDBTests(unittest.TestCase):

    def create_app(self):
        return create_test_app()

    def setUp(self):
        # Creates a new database for the unit test to use
        with self.create_app().app_context():
            db.create_all()


    def tearDown(self):
        # Ensures that the database is emptied for next unit test
        with self.create_app().app_context():
            db.session.remove()
            db.drop_all()


    def test_user_creation(self):
        user = User(username='Bob', email='t@t.com', password='password')
        db.session.add(user)
        db.session.commit()

        db_user = User.query.first()
        self.assertEqual(user.username, db_user.username)

    def test_empty_db(self):
        self.assertEqual(User.query.all(), [])
        self.assertEqual(Post.query.all(), [])


