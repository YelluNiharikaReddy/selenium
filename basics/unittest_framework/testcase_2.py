import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class searchEnginesTest(unittest.TestCase):
    def test_google(self):
        s = Service("C:\ Users\Dell\Desktop\chrome driver\chromedriver.exe")
        driver = webdriver.Chrome(service=s)
        driver.get("https://www.google.co.in/")
        print(driver.title)

    def test_bing(self):
        s = Service("C:\ Users\Dell\Desktop\chrome driver\chromedriver.exe")
        driver = webdriver.Chrome(service=s)
        driver.get("https://www.bing.com/")
        print(driver.title)

    if __name__ == "__main__":
        unittest.main()
    