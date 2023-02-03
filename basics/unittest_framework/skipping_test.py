import unittest

class Apptesting(unittest.TestCase):
    @unittest.SkipTest                   # skipping the test
    def test_search(self):
        print("this is search text")
    @unittest.skip("i am skipping this becuase it is not yet ready")       # skiping with reason
    def test_login(self):
        print("this is login text")
    @unittest.skipIf(1==1,"one is equal to one")                                # skipping with condition and reason
    def test_advance_search(self):
        print('this is adv search text')
    def test_postpaid(self):
        print("this is postpaid search text")
    def test_menu(self):
        print("this is menu text")
    def test_prepaid(self):
        print("this is prepaid text")