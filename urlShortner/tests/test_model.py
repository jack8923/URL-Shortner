from django.test import TestCase
from django.contrib.auth.models import User, auth
from ..models import shortURL
from django.urls import reverse


# Create your tests here.
class URLModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test', password='test1234', email='test@gmail.com')
        self.user.save()
        self.url = shortURL(user=self.user, original_url="https://github.com/jack8923/", short_url="my-repos")
        self.url.save()

    def tearDown(self):
        self.url.delete()
        self.user.delete()

    def test_short_url_max_length(self):
        url = shortURL.objects.get(id=1)
        max_length = url._meta.get_field('short_url').max_length
        self.assertEqual(max_length, 16)