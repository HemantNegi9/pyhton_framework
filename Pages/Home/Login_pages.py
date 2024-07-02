from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import logging
import utilities.custom_logger as cl



class login_page(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "//*[text()='Sign In']"
    _email_field = "email"
    _password_field = "login-password"
    _loginbutton = "login"

    # def get_login_link(self):
    #     return self.driver.find_element(By.XPATH,self._login_link)
    #
    # def get_email_field(self):
    #     return self.driver.find_element(By.ID, self._email_field)
    #
    # def get_password_field(self):
    #     return self.driver.find_element(By.ID, self._password_field)
    #
    # def get_login_button(self):
    #     return self.driver.find_element(By.ID,self._loginbutton)

    # Perform action on locators
    def click_login_link(self):
        self.elementClick(self._login_link, locatorType='xpath')

    def enter_email(self,email):
        self.sendKeys(email,self._email_field)

    def enter_password(self,password):
        self.sendKeys(password,self._password_field)

    def click_login_button(self):
        self.elementClick(self._loginbutton)

    def login(self,email="",password=""):
        self.click_login_link()
        # self.clearfield()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    def VerifyloginSuccessfully(self):
        result = self.isElementPresent("dropdownMenu1",locatorType ='id' )
        return result

    def Verifyinvalidlogin(self):
        result1 = self.isElementPresent('//*[contains(text(),"Incorrect login details. Please try again.")]',locatorType ='xpath')
        return result1

    def verifytitle(self):
        if "My Courses" in self.get_title():
            return True
        else:
            return False

    # def clearfield(self):
    #     emailFields = self._email_field(locator = self._email_field)
    #     emailFields.clear()
    #     passwordFields = self._password_field(locator=self._password_field)
    #     passwordFields.clear()


