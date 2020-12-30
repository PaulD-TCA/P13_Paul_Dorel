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

class SeleniumEditorialTests(StaticLiveServerTestCase):
    """
    3 functionals tests are done in this class.
    """
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        PATH = "/usr/local/bin/geckodriver"
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.headless = True
        firefox_options.add_argument('--window-size=1920x1080')
        cls.selenium = Firefox(executable_path=PATH, options=firefox_options)
