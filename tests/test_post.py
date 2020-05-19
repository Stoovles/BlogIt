import unittest
from blogit.models import Post
from blogit import db

class TestPost(unittest.TestCase):

    # def setUp(self) -> None:
    #     pass
    #
    # def tearDown(self) -> None:
    #     pass

    def test_post:
        post = Post(title='Post 1', content="Content 1", date_posted="2020-05-23")
        db.session.add(post)
        db.session.commit(post)

        self.assertEqual(Post.query.first(), post)
        self.assertEqual(Post.query.first.username(), post.title)
        self.assertEqual(Post.query.first.email(), post.content)
        self.assertEqual(Post.query.first.password(), post.date_posted)




