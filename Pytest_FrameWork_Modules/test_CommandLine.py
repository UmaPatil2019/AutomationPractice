import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestCLI:
    def test_login(self, setup):

        self.driver = setup
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        myWait = WebDriverWait(self.driver,5)
        Username = myWait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Username']")))
        Username.send_keys("Admin")

        Password = myWait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Password']")))
        Password.send_keys("admin123")

        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        time.sleep(3)
        try:
            self.status = self.driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']").is_displayed()
            self.driver.close()
            assert self.status == True
        except:
            self.driver.close()
            assert False