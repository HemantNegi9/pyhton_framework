from selenium import webdriver
from Pages.Home.Login_pages import login_page
import unittest
import pytest
import time


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classsetup(self, oneTimeSetUp):
        self.lp = login_page(self.driver)


    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("test@email.com", "abcabc")
        result1 = self.lp.VerifyloginSuccessfully()
        assert result1 == True
        result2 = self.lp.verifytitle()
        assert result2 == True

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login("test@email.com", "abcabcabc")
        result = self.lp.Verifyinvalidlogin()
        assert result == True
        time.sleep(3)


        # verify = driver.find_element(By.CLASS_NAME,'img-fluid')
        # if verify is not None:
        #     print("Logged in successfully")
        # else:
        #     print("login failed")



