import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class SVGEle:
    def svg(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://shiftsync.tricentis.com/")
        #driver.find_element(By.XPATH, "//input[@type='search']").click()
        # finds svg element

        #driver.find_element(By.XPATH,"(//*[local-name()='svg'])[10]")

        #finds child of svg element

        driver.find_element(By.XPATH,"(//*[name()='path'])[10]")
        time.sleep(5)
        driver.close()


svg_ele = SVGEle()
svg_ele.svg()