import unittest
class Test(unittest.TestCase):
    def test_name(self):
        # assertgreater
        self.assertGreater(100,10)
        # assert Greater Equal
        self.assertGreaterEqual(10,10)
        # assert Lesser
        self.assertLess(10,100)
        # assert less equal
        self.assertLessEqual(11,11)

    if __name__ == "__main__":
        unittest.main()
