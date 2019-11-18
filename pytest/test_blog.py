from django.test import TestCase
from selenium import webdriver
import time


# Create your tests here.
def test_setup():
    global driver
    driver = webdriver.Chrome("E:\Programming\Installers\Python\Repository\django_repo\drivers\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()


def test_about():
    driver.get("http://localhost:8000/")
    driver.find_element_by_name("about").click()
    time.sleep(4)
    driver.quit()


