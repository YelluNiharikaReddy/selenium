import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class Test(unittest.TestCase):
    def test_google(self):
        s = Service("C:\ Users\Dell\Desktop\chrome driver\chromedriver.exe")
        driver = webdriver.Chrome(service=s)
        driver.get("https://www.google.co.in/")
        actual_title = driver.title

        # assert equal
        self.assertEqual("Google",actual_title,"webpage title is not same")
        # assert not equal
        self.assertNotEqual("Google",actual_title , "title is same")
    if __name__ == "__main__":
        unittest.main()