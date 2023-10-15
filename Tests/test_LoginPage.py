import pytest
from Config.config import TestConfigData
from Pages.LoginPage import LoginPage
from Tests.test_Base import BaseTest


class Test_Login(BaseTest):

    def test_signin_button_visible(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.if_signin_button_visible()
        assert flag

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        HomePage = self.loginPage.do_login(TestConfigData.USER_NAME, TestConfigData.PASSWORD)
        assert HomePage.is_login_success()

