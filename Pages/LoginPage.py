from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Config.config import TestConfigData
from Pages.HomePage import HomePage


class LoginPage(BasePage):
    """ BY LOCATORS """
    USER_NAME = (By.ID,'username')
    PASSWORD = (By.ID, 'password')
    SUBMIT_BUTTON = (By.ID, 'submit')

    """ CONSTRUCTOR OF THE PAGE CLASS """
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestConfigData.TEST_URL)

    """ PAGE ACTIONS """

    def get_login_page_title(self,title):
        return self.get_login_page_title(self,title)

    def if_signin_button_visible(self):
        return self.is_visible(self.SUBMIT_BUTTON)

    def do_login(self,username,password):
        self.do_send_keys(self.USER_NAME,username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.SUBMIT_BUTTON)
        return HomePage(self.driver)

