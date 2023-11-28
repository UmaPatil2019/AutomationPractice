import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Alerts1():
    def alert1(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']").click()

        time.sleep(5)
        alertWindow = driver.switch_to.alert
        print(alertWindow.text)
        alertWindow.send_keys("Hello")
        #alertWindow.accept() #ok action on alert
        time.sleep(5)
        alertWindow.dismiss() #clicks on cancel button in prompt


alert1 = Alerts1()
alert1.alert1()