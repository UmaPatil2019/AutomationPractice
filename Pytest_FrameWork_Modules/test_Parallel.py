import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
class TestLogin:
    def test_login_chrome(self):
        from selenium.webdriver.chrome.service import Service as ChromeService
        from webdriver_manager.chrome import ChromeDriverManager
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        time.sleep(3)
        assert self.driver.title == "OrangeHRM"
        self.driver.quit()


    # def test_login_safari(self):
    #     from selenium.webdriver.safari.service import Service as SafariService
    #     self.browser = webdriver.Safari()
    #
    #     self.browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    #     time.sleep(3)
    #     self.browser.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
    #     time.sleep(3)
    #     self.browser.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
    #     time.sleep(3)
    #     self.browser.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
    #     time.sleep(3)
    #     assert self.browser.title == "OrangeHRM"
    #     self.browser.quit()





