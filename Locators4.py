import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Locators4_demo():
    def locators4(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://theautomationzone.blogspot.com/2020/07/xpath-practice.html#")
        time.sleep(3)

        #relativ xpath with and operator
        driver.find_element(By.XPATH,"//input[@id='mother_name' and @name='mother_name']").send_keys("uma")
        time.sleep(3)
        #relative xpath with or operator
        driver.find_element(By.XPATH,"//input[@id='father_name' or @type='text']").send_keys("abc")
        time.sleep(3)
        #relative xpath with contains operator.c
        driver.find_element(By.XPATH, "//button[contains(@onclick,'change()')]")
        time.sleep(5)
        driver.find_element(By.XPATH, "//button[contains(@onclick,'change2()')]").click()
        time.sleep(5)
        # # relative xpath with start with operator
        driver.find_element(By.XPATH,"//button[starts-with(@name,'submit')]").click()
        #relative xpath with text
        driver.find_element(By.XPATH,"//button[text()='random']").click()
        time.sleep(5)




        driver.close()
obj4 = Locators4_demo()
obj4.locators4()













