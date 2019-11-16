import pytest
from selenium import webdriver


@pytest. yield_fixture()

def setUp():
    print("Running methos level set up")
    yield
    print("Running method level tearDown")

@pytest.yield_fixture(scope="class")
def oneTimeSetUp(browser):
    print("Running one time set up")
    if  browser =='firefox':
        print("Running  test on FF")
    else:
        print("Running  test on Chrome")
    yield
    print("Running   one time tear down")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--ostype",help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return  request. config. getoption("--browser")

@pytest.fixture(scope="session")
def browser(request):
    return  request. config. getoption("--osType")

