import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class Test(unittest.TestCase):
    def test_name(self):
        list=["python","java","c#"]
        # assert In
        self.assertIn("python",list)          # pass
        self.assertIn("py",list)              # fail
        # assert Not In
        self.assertNotIn("python",list)       # fail
        self.assertNotIn("pyt",list)          # pass

