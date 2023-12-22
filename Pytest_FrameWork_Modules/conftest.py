import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    elif browser == "edge":
        pass #create edge related driver

    elif browser == 'firefox':
        pass #create firefox related driver

    return driver

def pytest_addoption(parser):
    parser.addoption("--browser") # this will get the browser name from terminal command

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser") #this will return the browser name from addoption method to setup method

#to customize html report, remove default template and add customized options. These functions can be found in Python documentation
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'Orange HRM'
#     config._metadata['Module Name'] = 'Login Module'
#     config._metadata['Tester Name'] = 'Uma'
#
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_Home", None)
#     metadata.pop("Plugins", None)

#pass any browsername in terminal
# pytest -v -s Pytest_FrameWork_Modules/test_CommandLine.py --browser chrome


    # print("Launching browser...")
    # print("Open Application...")
    # # yield prints at the end of test methods
    # yield
    # print("Closing browser....")






