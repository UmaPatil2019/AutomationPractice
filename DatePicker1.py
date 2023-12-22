import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException

class DatePick1():
    def datePick1(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        #myWait = WebDriverWait(driver, 10)

        ## Example of when date picker is available and input the date in the box with send keys
        driver.get("https://jqueryui.com/datepicker/")
        # #as there is only one frame, use index 0 directly
        driver.switch_to.frame(0)
        # #driver.find_element(By.ID, "datepicker").send_keys("09/30/2024")
        # see_date = myWait.until(EC.presence_of_element_located((By.ID, "datepicker")))
        # see_date.send_keys("09/30/2024")
        # time.sleep(3)


        ##Example of when date picker is available, but have to do select from the date picker instead of inputting the date
        #to select future dates
        # month = "November"
        # day = "29"
        # year = "2024"
        # driver.find_element(By.ID, "datepicker").click()




        # while True:
        #     mon = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
        #     yr = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
        #     if month==mon and year==yr:
        #         break
        #     else:
        #         driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[2]/span").click()
        #
        # dates = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
        #
        # for date in dates:
        #     if date.text == day:
        #         date.click()
        #         time.sleep(3)


        #to select past dates

        month = "January"
        day = "29"
        year = "2022"
        driver.find_element(By.ID, "datepicker").click()

        while True:
            mon = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
            yr = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
            if month == mon and year == yr:
                break
            else:
                #select first anchor to select back arrow
                driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[1]/span").click()

        dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

        for date in dates:
            if date.text == day:
                date.click()
                time.sleep(3)


objDate1 = DatePick1()
objDate1.datePick1()