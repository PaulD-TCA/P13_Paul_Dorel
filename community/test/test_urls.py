from django.test import SimpleTestCase
from django.urls import reverse, resolve
from community.views import messages, my_offers


class TestUrls(SimpleTestCase):
    def test_design_list_url_resolved(self):
        url = reverse('messages')
        self.assertEquals(resolve(url).func, messages)

    def test_my_offers_presentation_url_resolved(self):
        url = reverse('my_offers')
        self.assertEquals(resolve(url).func, my_offers)
