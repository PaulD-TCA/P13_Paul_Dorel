from django.test import SimpleTestCase
from django.urls import reverse, resolve
from community.views import messages, my_offers, email_user, make_offer, offers_on_design


class TestUrls(SimpleTestCase):
    def test_message_url_resolved(self):
        url = reverse('messages')
        self.assertEquals(resolve(url).func, messages)

    def test_my_offers_url_resolved(self):
        url = reverse('my_offers')
        self.assertEquals(resolve(url).func, my_offers)

    def test_email_user_url_resolved(self):
        url = reverse('email_user', args=['1'])
        self.assertEquals(resolve(url).func, email_user)

    def test_make_offer_url_resolved(self):
        url = reverse('make_offer', args=['1'])
        self.assertEquals(resolve(url).func, make_offer)

    def test_offers_on_design_url_resolved(self):
        url = reverse('offers_on_design', args=['1'])
        self.assertEquals(resolve(url).func, offers_on_design)
