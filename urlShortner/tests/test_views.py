from django.test import TestCase
from django.contrib.auth.models import User, auth
from ..models import shortURL
from django.urls import reverse


# Create your tests here.
class DashboardView(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(first_name='user', last_name='1', username='test', password='test1234',
                                             email='test@gmail.com')
        self.user.save()
        self.url = shortURL(user=self.user, original_url="https://github.com/jack8923/", short_url="my-repos")
        self.url.save()

    def tearDown(self):
        self.url.delete()
        self.user.delete()

    def test_not_logged_in_uses_correct_response(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)                             # to check status
        self.assertTemplateUsed(response, 'home.html')                          # to check template

        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)                             # to check status
        self.assertTemplateUsed(response, 'login.html')                         # to check template

        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)                             # to check status
        self.assertTemplateUsed(response, 'register.html')                      # to check template

        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)                             # to check status
        self.assertRedirects(response, '/login?next=%2Fdashboard/')


    def test_logged_in_uses_correct_response(self):
        login = self.client.login(username='test', password='test1234')

        response = self.client.get(reverse('home'))
        self.assertEqual(str(response.context['user']), 'test')                # to check if correct user is logged in
        self.assertEqual(response.status_code, 200)                             # to check status
        self.assertTemplateUsed(response, 'home.html')                          # to check template

        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)                             # to check status
        self.assertTemplateUsed(response, 'dashboard.html')                     # to check template