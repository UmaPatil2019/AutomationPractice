import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Alerts2():
    def alert2(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://mypage.rediff.com/")
        time.sleep(5)
        driver.find_element(By.XPATH, "//tr/td/input[@type='submit']").click()

        Prompt = driver.switch_to.alert
        print(Prompt.text)
        Prompt.accept()

obj1 = Alerts2()
obj1.alert2()