import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Alerts3():
    def alert3(self):

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        #url without username/password
        #driver.get("https://the-internet.herokuapp.com/basic_auth")
        #url with username:password to bypass the alert in authentication pop up
        driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
        time.sleep(5)

obj3 = Alerts3()
obj3.alert3()