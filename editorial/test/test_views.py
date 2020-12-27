from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from design.models import Message, Offer, Design

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.project_presentation_url = reverse('project_presentation')

    def test_home_GET(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'editorial/home.html')

    def test_project_presentation_GET(self):
        response = self.client.get(self.project_presentation_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'editorial/project_presentation.html')
