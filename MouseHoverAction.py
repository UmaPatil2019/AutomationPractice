import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


#import ActionChains package to work on mouse hovers
class MouseHover():
    def mousehover1(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://practice.expandtesting.com/hovers")
        image1 = driver.find_element(By.XPATH, "//div[@class='container']//div[1]//img[1]")
        time.sleep(3)
        Profile = driver.find_element(By.XPATH, "//main[@class='flex-shrink-0 py-3']//div[@class='container']//div[1]//div[1]//a[1]")
        Action = ActionChains(driver)
        Action.move_to_element(image1).move_to_element(Profile).click().perform()
        time.sleep(3)


MHObj = MouseHover()
MHObj.mousehover1()



