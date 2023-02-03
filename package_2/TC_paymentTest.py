import unittest

class PaymentsTest(unittest.TestCase):
    def test_paymentsinrupees(self):
        print("this is payment in  rupees text")
        self.assertTrue(True)

    def test_paymentsindollor(self):
        print("this is payment in dollor text")
        self.assertTrue(True)
        
    if __name__ == "__main__":
        unittest.main()
