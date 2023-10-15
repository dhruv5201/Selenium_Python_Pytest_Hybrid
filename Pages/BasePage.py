from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Config.config import TestConfigData

""" This is Base Class parents of all Pages"""

class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver,TestConfigData.WAIT_TIME_ACTION).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self,by_locator, text):
        WebDriverWait(self.driver, TestConfigData.WAIT_TIME_ACTION).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self,by_locator):
        element = WebDriverWait(self.driver, TestConfigData.WAIT_TIME_ACTION).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self,by_locator):
        element = WebDriverWait(self.driver, TestConfigData.WAIT_TIME_ACTION).until(EC.visibility_of_element_located(by_locator))
        return bool(element)







