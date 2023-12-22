from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException
import time

class Xpath_Practice1():
    def xpath1(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        myWait = WebDriverWait(driver, 10, poll_frequency=2,
                               ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                                   ElementNotSelectableException,
                                                   Exception])  # explicit wait declaration
        driver.get("https://testautomationpractice.blogspot.com/")

        # web table with checkbox
        # rows = len(driver.find_elements(By.XPATH, "//table[@id='productTable']//tbody/tr"))
        # cols = len(driver.find_elements(By.XPATH, "//table[@id='productTable']//tbody/tr/td"))
        # checboxes_1 = driver.find_elements(By.XPATH, "//table[@id='productTable']//tbody/tr/td[4]")
        # ID = driver.find_elements(By.XPATH, "//table[@id='productTable']//tbody/tr/td[1]")
        # #
        # # for row in range(2, rows+1):
        # #     for col in range(1, cols+1):
        #
        # for i in checboxes_1:
        #     if ID==2:
        #         i.click()
        #
        # time.sleep(5)

        # searchbox
        driver.find_element(By.XPATH, "//input[@id='Wikipedia1_wikipedia-search-input']").send_keys("Drop")
        driver.find_element(By.XPATH, "//input[@type='submit']").click()
        search_results = myWait.until(EC.visibility_of_any_elements_located((By.XPATH, "//div[@id='wikipedia-search-result-link']/a")))

        for link in search_results:
            print(link.text)


        # Prompt
        driver.find_element(By.XPATH, "//button[text()='Prompt']").click()
        time.sleep(3)
        alertWindow3 = driver.switch_to.alert

        print(alertWindow3.text)
        time.sleep(3)

        alertWindow3.send_keys(" ")
        alertWindow3.send_keys("Uma")
        time.sleep(3)
        alertWindow3.accept()
        time.sleep(5)


    #Datepicker in the iframe
        # frame = driver.find_element(By.XPATH, "(//iframe[@id='frame-one796456169'])[1]")
        # driver.switch_to.frame(frame)
        # driver.find_element(By.XPATH, "//span[@class='icon_calendar']").click()
        # month2 = "January"
        # day2 = "29"
        # year2 = "2024"
        #
        # # while True:
        # #
        # #     month1 = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
        # #     year1 = driver.find_element(By.XPATH, "//select[@class='ui-datepicker-year']").text
        # #     if month1 == month2 and year1 == year2:
        # #         break
        # #     else:
        # #         driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']").click()
        # #
        # # dates_Calender = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/td/a")
        # # for i in dates_Calender:
        # #     if i == day2:
        # #         i.click()
        # #         time.sleep(3)
        #
        # # svg element
        #
        # #driver.find_element(By.XPATH, "(//*[local-name() = 'svg'])").click()


Practice_Obj2 = Xpath_Practice1()
Practice_Obj2.xpath1()


