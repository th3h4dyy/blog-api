from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Post


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = get_user_model().objects.create(
            username="testuser", email="testemail@test.com", password="testpassword"
        )
        cls.post = Post.objects.create(
            title="test post", body="test body", author=cls.user
        )

    def test_post_modal(self):
        self.assertEqual(self.post.title, "test post")
        self.assertEqual(self.post.body, "test body")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(str(self.post), "test post")
