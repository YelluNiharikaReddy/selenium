import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class Test(unittest.TestCase):
    def test_Name(self):
        s=Service("C:\ Users\Dell\Desktop\chrome driver\chromedriver.exe")
        driver = webdriver.Chrome(service=s)
        driver.get("https://www.google.co.in/")
        actual_title= driver.title
    # assertion true
        self.assertTrue(actual_title == "Google","title is not equal")
    # assertion False
        self.assertFalse(actual_title=="google","title is equal ")
    if __name__ == "__main__":
        unittest.main()

