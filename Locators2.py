import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
#class name and tag name locators are used to find group of html elements
class Locators2_demo():
    def locators(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://demo.nopcommerce.com/")
        time.sleep(3)
        driver.find_element(By.LINK_TEXT,"Register").click()
        time.sleep(3)
        driver.find_element(By.PARTIAL_LINK_TEXT,"Wish").click()

        sliders = driver.find_elements(By.CLASS_NAME,"title")
        time.sleep(3)
        print(len(sliders))
        for i in sliders:
            print(i.text)
        links = driver.find_elements(By.TAG_NAME,'a')
        print(len(links))
        for i in links:
            print(i.text)
        driver.close()
obj1 = Locators2_demo()
obj1.locators()




