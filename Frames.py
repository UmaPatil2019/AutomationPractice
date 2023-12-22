import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Frames1():
    def frame1(self):

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://demo.automationtesting.in/Frames.html")

#frames can be obtained by using frame name, frame ID, webelements
#always quit from one frame to main page, before switching to another one, if they are not nested within one inside another

        driver.find_element(By.XPATH, "//a[normalize-space()='Iframe with in an Iframe']").click()

        #switch to outerframe
        outerFrame = driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']")
        driver.switch_to.frame(outerFrame)

        #switch to inner frame
        innerFrame = driver.find_element(By.XPATH, "//iframe[normalize-space()='<p>Your browser does not support iframes.</p>']")
        driver.switch_to.frame(innerFrame)

        #go to input box inside the frame
        driver.find_element(By.XPATH, "//input[@type='text']").send_keys("welcome")
        time.sleep(5)

        # #switch to outerframe(parent frame) from inner frame
        # driver.switch_to.parent_frame()
        # #switch to main webpage from out of all the frames
        # driver.switch_to.default_content()

objFrame1 = Frames1()
objFrame1.frame1()