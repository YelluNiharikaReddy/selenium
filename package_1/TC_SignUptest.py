import unittest


class SignupTest(unittest.TestCase):
    def test_signupbyemail(self):
        print("this is sign up eamil text")
        self.assertTrue(True)

    def test_signupbyfacebook(self):
        print("this is signup by facebook text")
        self.assertTrue(True)

    def test_signupbytwitter(self):
        print("this is signup by twitter")
        self.assertTrue(True)

    if __name__ == "__main__":
        unittest.main()

