from django.test import SimpleTestCase
from django.urls import reverse, resolve
from editorial.views import home, project_presentation


class TestUrls(SimpleTestCase):
    def test_home_url_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)

    def test_project_presentation_url_resolved(self):
        url = reverse('project_presentation')
        self.assertEquals(resolve(url).func, project_presentation)
