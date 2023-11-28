import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class locators3_demo():
    def locators3(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        driver.get("https://www.facebook.com/")
        time.sleep(3)

        #tag&id css selector
        driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("abc") #username input
        # tag&attribute css selector
        #driver.find_element(By.CSS_SELECTOR, "input[name=pass]").send_keys("defghi") #password input
        # tag, class & attribute selector
        driver.find_element(By.CSS_SELECTOR, "input.inputtext[name=pass]").send_keys("jdglkdsj")
        time.sleep(3)
        #tag&class css selector()
        driver.find_element(By.CSS_SELECTOR,"button._42ft").click() #login button



obj2 = locators3_demo()
obj2.locators3()
