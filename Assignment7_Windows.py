import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


class YatraWindows():
    def Windows(self):
        option = Options()
        option.add_argument("--disable-notifications")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=option)
        driver.implicitly_wait(5)

        # navigate to Yatra website
        driver.get("https://www.yatra.com/")

        # Parent window ID(Yatra main page)
        Parent_Window = driver.current_window_handle

        # Maximize the wimdow
        driver.maximize_window()

        # Get xpath of Yatra Specials View All
        Yatra_Specials_Window = driver.find_element(By.XPATH, "//a[normalize-space()='View All']")

        # click on Yatra specials to navigate to that window
        Yatra_Specials_Window.click()
        # time.sleep(5)

        # Get window Ids of all windows. Parent ID is at [0], child at [1]
        Window_Ids = driver.window_handles

        for ID in Window_Ids:
            # check if it's not parent window
            if ID != Parent_Window:
                # switch driver focus to child window
                driver.switch_to.window(ID)
                # Click on International fligts tab
                driver.find_element(By.XPATH, "//ul[@id='offer-box-shadow']/li[2]/a").click()
                break

        # Switch back to parent window(Yatra home page)
        driver.switch_to.window(Parent_Window)
        time.sleep(3)
        # click on Yatra specials again
        Yatra_Specials_Window.click()
        time.sleep(5)
        # close all browser windows
        driver.quit()


Win_Obj = YatraWindows()
Win_Obj.Windows()


