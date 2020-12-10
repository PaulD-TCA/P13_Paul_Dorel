from django.test import SimpleTestCase
from django.urls import reverse, resolve
from user.views import user_login, user_logout, user_signup


class TestUrls(SimpleTestCase):
    def test_user_login_url_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, user_login)

    def test_user_logout_presentation_url_resolved(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, user_logout)

    # def test_user_signup_url_resolved(self):
    #     url = reverse('signup')
    #     self.assertEquals(resolve(url).func, user_signup)
