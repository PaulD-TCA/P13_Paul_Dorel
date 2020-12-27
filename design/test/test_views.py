from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from design.models import Message, Offer, Design

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.design_list_url = reverse('design_list')
        self.upload_design_url = reverse('upload_design')
        self.my_design_url = reverse('my_design')

    def test_design_list_GET(self):
        response = self.client.get(self.design_list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'design/design_list.html')

    def test_upload_design_GET(self):
        response = self.client.get(self.upload_design_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'design/upload_design.html')

    def test_my_design_GET(self):
        response = self.client.get(self.my_design_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'design/my_design.html')
