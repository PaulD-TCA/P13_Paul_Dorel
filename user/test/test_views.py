from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from design.models import Message, Offer, Design

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user_login_url = reverse('login')
        self.user_logout_url = reverse('logout')
        self.user_signup_url = reverse('signup')
        self.personal_datas_url = reverse('personal_datas')

    def test_user_login_GET(self):
        response = self.client.get(self.user_login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/login.html')

    # def test_user_logout_GET(self):
    #     response = self.client.get(self.user_logout_url)
    #     self.assertEquals(response.status_code, 302)
    #     self.assertTemplateUsed(response, 'editorial/home.html')

    def test_user_signup_GET(self):
        response = self.client.get(self.user_signup_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/signup.html')

    def test_personal_datas_GET(self):
        response = self.client.get(self.personal_datas_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/personal_datas.html')
