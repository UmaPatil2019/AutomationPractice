import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class KeyboardActions():
    def keyboard(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.implicitly_wait(5)

        driver.get("https://text-compare.com/")
        driver.maximize_window()
        input_box1 = driver.find_element(By.XPATH, "//textarea[@name='text1']").send_keys("Welcome to selenium")
        input_box2 = driver.find_element(By.XPATH, "//textarea[@name='text2']")
        act = ActionChains(driver)
        #Cmnd A to select input1 text
        act.key_down(Keys.COMMAND).send_keys("a").key_up(Keys.COMMAND).perform()
        #Command C to copy text
        act.key_down(Keys.COMMAND).send_keys("c").key_up(Keys.COMMAND).perform()
        #Press Tab to go to input text area 2
        act.send_keys(Keys.TAB).perform()
        #Command v to paste text from input1 to input2
        act.key_down(Keys.COMMAND).send_keys("v").key_up(Keys.COMMAND).perform()




MouseActions_Obj = KeyboardActions()
MouseActions_Obj.keyboard()