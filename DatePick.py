# import time
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support import expected_conditions as E
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException


# class DatePick1():
#     def Calen_prac(self):
#         driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#         W = WebDriverWait(driver, 10)
#         driver.get("https://testautomationpractice.blogspot.com/")
#         user_date = W.until(E.element_to_be_clickable((By.XPATH, "//input[@id='datepicker']")))
#         user_date.click()
#         time.sleep(4)
#         date_tabl = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']//tbody[1]//td/a")
#
#         for today_date in date_tabl:
#             #print(today_date.text)
#             if today_date.text == '8':
#                 today_date.click()
#                 time.sleep(4)
#
#
# Obj2 = DatePick1()
# Obj2.Calen_prac()

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as E


class FormAuto:
    # def init(self):
    #     self.driver=None

    def intialize_driver(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def navigate_to_website(self, url):
        self.driver.get(url)
        print(self.driver.title)

    def Calen_prac(self):
        user_date = W(self.driver, 10).until(E.element_to_be_clickable((By.XPATH, "//input[@id='datepicker']")))
        user_date.click()
        time.sleep(4)
        date_tabl=self.driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//tbody[1]//td/a")

        for today_date in date_tabl:
            #print(today_date.text)
            if today_date.text == "8":
               today_date.click()
               time.sleep(4)


        user_date.screenshot(".\test.png")
        #user_date.save_screenshot(".\test1.png")
        time.sleep(5)


form_calenpract=FormAuto()
form_calenpract.intialize_driver()
form_calenpract.navigate_to_website("https://testautomationpractice.blogspot.com/")
form_calenpract.Calen_prac()