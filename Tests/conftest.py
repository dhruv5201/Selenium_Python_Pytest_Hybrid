import pytest
from selenium import webdriver
from Config.config import TestConfigData

@pytest.fixture(params = ['chrome'],scope = 'class')
def init_driver(request):
    if request.param == 'chrome':
        web_driver = webdriver.Chrome()
    if request.param == 'firefox':
        web_driver = webdriver.Chrome(TestConfigData.FIREFOX_EXECUTABLE_PATH)
    request.cls.driver = web_driver
    yield
    web_driver.quit()


