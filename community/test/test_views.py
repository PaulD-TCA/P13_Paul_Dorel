from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from design.models import Message, Offer, Design

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('messages')
        self.my_offers_url = reverse('my_offers')
        self.email_user_url = reverse('email_user', args=['1'])
        self.make_offer_url = reverse('make_offer', args=['1'])
        self.offers_on_design_url = reverse('offers_on_design', args=['1'])

    def test_messages_GET(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'community/messages.html')

    def test_my_offers_GET(self):
        response = self.client.get(self.my_offers_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'community/my_offers.html')

    def test_email_user_GET(self):
        response = self.client.get(self.email_user_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'community/email_to_user.html')

    def test_make_offer_GET(self):
        response = self.client.get(self.make_offer_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'community/make_offer.html')

    def test_offers_on_design_GET(self):
        response = self.client.get(self.offers_on_design_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'community/design_offer.html')
