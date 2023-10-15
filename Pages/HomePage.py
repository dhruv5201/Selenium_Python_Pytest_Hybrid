from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Config.config import TestConfigData

class HomePage(BasePage):
    """ BY LOCATORS """
    LOGOUT_BUTTON = (By.XPATH,"//a[contains(text(),'Log out')]")
    LOGIN_SUCCESS_MESSAGE = (By.XPATH, "//h1[contains(text(),'Logged In Successfully')]")


    """ CONSTRUCTOR OF THE PAGE CLASS """
    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(TestConfigData.TEST_URL)

    """ PAGE ACTIONS """
    def is_logout_button_visible(self):
        return self.is_visible(self.LOGOUT_BUTTON)

    def is_login_success(self):
        return self.is_visible(self.LOGIN_SUCCESS_MESSAGE)