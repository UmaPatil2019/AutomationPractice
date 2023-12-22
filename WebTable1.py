import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
#static table
class WebTable1():
    def Table1(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://testautomationpractice.blogspot.com/")
        #count number of rows and columns
        numberOfRows = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr"))
        print(numberOfRows)
        numberOfColumns = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr[1]/th"))
        print(numberOfColumns)


        #pass the row and column numbers to get specific value
        data = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[5]/td[1]").text
        print(data)

        #read all rows and columns data
        for row in range(2, numberOfRows+1):
            for col in range(1, numberOfColumns+1):
                data = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(row)+"]/td["+str(col)+"]").text
                print(data, end='   ')
            print()

        #read data based on certain condition(list book names by author Mukesh)
        for row in range(2,numberOfRows+1):
            authorName = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(row)+"]//td[2]").text
            if authorName== "Mukesh":
                bookName = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(row)+"]//td[1]").text
                Price = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(row) + "]//td[4]").text
                print(bookName, "    ", authorName, "      " + Price)





objWBTable = WebTable1()
objWBTable.Table1()

