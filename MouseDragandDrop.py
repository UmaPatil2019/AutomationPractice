from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


#import ActionChains package to work on mouse hovers and clicks, drag/drop
class MouseDragAndDrop():
    def DragandDrop(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
        Rome_sourceElement = driver.find_element(By.ID, "box6")
        Italy_DestinationElement = driver.find_element(By.ID, "box106")

        DragAndDrop = ActionChains(driver)

        DragAndDrop.drag_and_drop(Rome_sourceElement, Italy_DestinationElement).perform()





DragandDropObj1 = MouseDragAndDrop()
DragandDropObj1.DragandDrop()




