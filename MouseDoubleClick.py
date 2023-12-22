from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


#import ActionChains package to work on mouse hovers and clicks, drag/drop
class MouseDoubleClick():
    def mouseDoubleClick(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
        driver.switch_to.frame("iframeResult")
        field1 = driver.find_element(By.XPATH, "//input[@id='field1']")
        field1.clear()
        field1.send_keys("Welcome")

        CopyText = driver.find_element(By.XPATH, "//button[normalize-space()='Copy Text']")

        DoubleClick = ActionChains(driver)

        DoubleClick.double_click(CopyText).perform()


DCmouse = MouseDoubleClick()
DCmouse.mouseDoubleClick()
