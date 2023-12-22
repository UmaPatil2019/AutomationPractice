import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestParameter:
    @pytest.mark.parametrize('user,pwd',[("Admin", "admin123"),("adm","admin123"),("Admin", "adm"),("adm", "adm")])
    def test_parameterization(self, user, pwd):
        from selenium.webdriver.chrome.service import Service as ChromeService
        from webdriver_manager.chrome import ChromeDriverManager
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys(user)
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(pwd)
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        time.sleep(3)
        try:
            self.status = self.driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']").is_displayed()
            self.driver.close()
            assert self.status == True
        except:
            self.driver.close()
            assert False