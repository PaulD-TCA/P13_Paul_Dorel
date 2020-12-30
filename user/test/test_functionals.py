from selenium import webdriver
from selenium.webdriver import Firefox
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from design.models import Design
import os

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class SeleniumUserTests(StaticLiveServerTestCase):
    """
    3 functionals tests are done in this class.
    """
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        PATH = "/usr/local/bin/geckodriver"
        firefox_options = webdriver.FirefoxOptions()
        # firefox_options.headless = True
        firefox_options.add_argument('--window-size=1920x1080')
        cls.selenium = Firefox(executable_path=PATH, options=firefox_options)

    # def test_a_register(self):
    #     """
    #     This test will check if a new user can be created.
    #     """
    #     self.server = self.live_server_url+"/user/signup/"
    #     self.selenium.get(self.server)
    #     self.username = self.selenium.find_element_by_name("username")
    #     self.password1 = self.selenium.find_element_by_name("password1")
    #     self.password2 = self.selenium.find_element_by_name("password2")
    #     self.creation_button = self.selenium.find_element_by_id("creation_btn")
    #     self.username.send_keys("Armelle")
    #     self.password1.send_keys("wxcvbn1234")
    #     self.password2.send_keys("wxcvbn1234")
    #     self.creation_button.submit()
    #     self.confirmation = WebDriverWait(self.selenium, 10).until(
    #         expected_conditions.presence_of_element_located((By.ID, "messages")))
    #     self.assertEqual(self.confirmation.text, "Le compte à été créé pourArmelle")
