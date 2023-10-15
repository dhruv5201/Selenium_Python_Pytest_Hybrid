import pytest
from Config.config import TestConfigData
from Pages.LoginPage import LoginPage
from Tests.test_Base import BaseTest


class Test_HomePage(BaseTest):

    def test_logout_button_visible(self):
        self.loginPage = LoginPage(self.driver)
        HomePage = self.loginPage.do_login(TestConfigData.USER_NAME,TestConfigData.PASSWORD)
        assert HomePage.is_logout_button_visible()

    def test_is_login_success(self):
        self.loginPage = LoginPage(self.driver)
        HomePage = self.loginPage.do_login(TestConfigData.USER_NAME, TestConfigData.PASSWORD)
        assert HomePage.is_login_success()