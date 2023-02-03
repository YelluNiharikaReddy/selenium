import unittest


class LoginTest(unittest.TestCase):
    def test_loginbyemail(self):
        print("this is login by email text ")
        self.assertTrue(True)

    def test_loginbyfacebook(self):
        print("this is login by facebook text")
        self.assertTrue(True)

    def test_loginbytwitter(self):
        print("this is login by twitter text")
        self.assertTrue(True)

    if __name__ == "__main__":
        unittest.main()