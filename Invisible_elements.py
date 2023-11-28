import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
class invisible_ele():
    def invi_ele(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.flipkart.com/")
        # object of ActionChains
        a = ActionChains(driver)
        driver.find_element(By.XPATH, "//span[@role='button']").click()
        #identify element
        driver.find_element(By.XPATH, "//span[contains(text(),'Electronics')]").click()


        time.sleep(5)
        m = driver.find_element(By.XPATH, "(//a[normalize-space()='Computer Peripherals'])[1]")
        # hover over element
        a.move_to_element(m).perform()
        time.sleep(5)
        driver.find_element(By.LINK_TEXT, "Monitors").click()
        time.sleep(5)
        driver.close()

inv1 = invisible_ele()
inv1.invi_ele()
