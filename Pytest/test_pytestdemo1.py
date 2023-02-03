import pytest


@pytest.fixture()
def SetUp():
    print("once before every method")
    yield
    print("once after every method")

def testmethod1():
    print("this is method 1")
def testmethod2():
    print("this is method 2")