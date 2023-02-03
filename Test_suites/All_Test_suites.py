import unittest
from package_1.TC_logintest import LoginTest
from package_1.TC_SignUptest import SignupTest
from package_2.TC_paymentTest import PaymentsTest
from package_2.TC_paymentsReturnsTest import PaymentReturnsTest

TC1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
TC2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
TC3 = unittest.TestLoader().loadTestsFromTestCase(PaymentsTest)
TC4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)

# creating test suites
SanityTestSuite = unittest.TestSuite([TC1,TC2])                    # sanitytestsuite = only login and log out
unittest.TextTestRunner().run(SanityTestSuite)

FunctionalSuite = unittest.TestSuite([TC3,TC4])                    # functionalTestsuite = only payments test case
unittest.TextTestRunner().run(FunctionalSuite)

MasterSuite = unittest.TestSuite([TC1,TC2,TC3,TC4])                 # all type of tests
unittest.TextTestRunner().run(MasterSuite)
