from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class WC():
    def Webdriver_Commands(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.saucedemo.com/") #opening the application URL
        print(driver.title) #to capture title of the current pwebpage
        print(driver.current_url) #to capture current URL of the web page
        print(driver.page_source) #to capture html source code of the page
        driver.close()

obj6 = WC()
obj6.Webdriver_Commands()