from selenium import webdriver
import os
import platform


def test_setUp():
    directory = os.getcwd()
    chrome_driver_name = 'chromedriver' if platform.system() == 'Linux' else 'chromedriver.exe'
    print(directory)
    chrome_driver_directory = directory + "/drivers/" + chrome_driver_name
    print(chrome_driver_directory)
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-extensions')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    global driver
    driver = webdriver.Chrome(options=options, executable_path=chrome_driver_directory)
    driver.set_page_load_timeout(10)


def test_about():
    driver.get("http://localhost:8000/")
    driver.find_element_by_id("about").click()


def test_tearDown():
    driver.quit()
