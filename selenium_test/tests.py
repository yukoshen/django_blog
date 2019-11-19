from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
import os
import platform


class SeleniumTest(StaticLiveServerTestCase):

    def setUp(self):
        directory = os.getcwd()
        chrome_driver_name = 'chromedriver' if platform.system() == 'Linux' else 'chromedriver.exe'
        chrome_driver_directory = directory + "/selenium_test/drivers/" + chrome_driver_name
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-extensions')
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        self.browser = webdriver.Chrome(options=options, executable_path=chrome_driver_directory)
        self.browser.set_page_load_timeout(10)

    def tearDown(self):
        self.browser.close()

    def test_about(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id("about").click()