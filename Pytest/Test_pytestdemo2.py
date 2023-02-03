import pytest

@pytest.yield_fixture()

def SetUp():
    print("once before every method")
    yield
    print("once after every method")

def testloginfacebook():
    print("this is facebook login ")
def testbyemail():
    print("this is email login")


