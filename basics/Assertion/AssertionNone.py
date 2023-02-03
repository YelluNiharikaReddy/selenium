import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class Test(unittest.TestCase):
    def test_name(self):
        s = Service("C:\ Users\Dell\Desktop\chrome driver\chromedriver.exe")
        driver = webdriver.Chrome(service=s)
        driver.get("https://www.google.co.in/")
        actual_title = driver.title
        # assert none
        self.assertIsNone(driver,"there is a title")
        # assert not none
        self.assertIsNotNone(driver,"there is no  title")
