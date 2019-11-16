import Demo.pom.login import Login
import pytest
from selenium import webdriver


@pytest. mark.usefixtures("onetimesetup","setUp")
class TestClassDemo():


    @pytest.fixture(autocase=True)
    def classSetup (self):
        self.log_in= Login()
        Print("Class level set up of  py pi org")
         yield
        print(" Logging out of py pi org")
