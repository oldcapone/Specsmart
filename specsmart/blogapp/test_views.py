from django.test import Client
from django.test import TestCase
from faker import Faker
from usersapp.models import BlogUser


class ViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.fake = Faker()

    def test_statuses(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        # Что мы можем проверить
        response = self.client.get('/contacts/')
        self.assertEqual(response.status_code, 200)

        # post зарос
        response = self.client.post('/contact/',
                                    {'name': self.fake.name(), 'message': self.fake.text(),
                                     'email': self.fake.email()})

        self.assertEqual(response.status_code, 404)

        # Какие данные передаются в контексте
        response = self.client.get('/')
        self.assertFalse('posts' in response.context)

    def test_login_required(self):
        BlogUser.objects.create_user(username='test_user', password='FF1234567')
        # Он не вошел
        response = self.client.get('/users/login/')
        self.assertEqual(response.status_code, 200)

        # Логиним
        self.client.login(username='test_user', password='FF1234567')

        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 302)