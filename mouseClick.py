import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


#import ActionChains package to work on mouse hovers and clicks, drag/drop
class MouseClick():
    def mouseclick1(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.implicitly_wait(3)
        driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
        button = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")

        RightClick_Action = ActionChains(driver)
        RightClick_Action.context_click(button).perform()

RCMouseobj1 = MouseClick()
RCMouseobj1.mouseclick1()