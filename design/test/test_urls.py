from django.test import SimpleTestCase
from django.urls import reverse, resolve
from design.views import design_list, upload_design, my_design


class TestUrls(SimpleTestCase):
    def test_design_list_url_resolved(self):
        url = reverse('design_list')
        self.assertEquals(resolve(url).func, design_list)

    def test_upload_design_presentation_url_resolved(self):
        url = reverse('upload_design')
        self.assertEquals(resolve(url).func, upload_design)

    def test_my_design_url_resolved(self):
        url = reverse('my_design')
        self.assertEquals(resolve(url).func, my_design)
