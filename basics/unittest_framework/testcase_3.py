import unittest
from selenium import webdriver



class AppTesting(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("this is login text")
    @classmethod
    def tearDown(self):
        print("this is logout text")
    @classmethod
    def setUpClass(cls):
        print("open application")
    @classmethod
    def tearDownClass(cls) :
        print("close apllication")
    @classmethod
    def setUpModule(cls):
        print("set up module")
    @classmethod
    def tearDownModule(cls):
        print("class module")
        
    def test_search(self):
        print("this is search text")
    def test_advanced_search(self):
        print("this is adv serach text")
    def test_post_paid(self):
        print("this is postpaid text")
if __name__ == "__main__":
    unittest.main()