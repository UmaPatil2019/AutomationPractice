from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

import time

class Xpath_Practice():
    def xpath(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://testautomationpractice.blogspot.com/")

        #input text
        driver.find_element(By.XPATH, "//input[@id='name']").send_keys("uma")
        driver.find_element(By.XPATH,"//input[@id='email']" ).send_keys("abc@gmail.com")
        driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("1234567")
        driver.find_element(By.XPATH, "//textarea[@id='textarea']").send_keys("2134 lawrence ave 98732")


        #radio buttons
        #driver.find_element(By.XPATH, "//div[@class='form-check form-check-inline']/child::input[@id='male']").click()
        driver.find_element(By.XPATH, "//label[@class='form-check-label']/preceding-sibling::input[@id='female']").click()

        #checkboxes
        checkboxes = driver.find_elements(By.XPATH, "//input[@id='friday' or @id='saturday']")
        for i in checkboxes:
            i.click()

        #Dropdown; two methods to select option, one from XPath country option/click, another with Select class and its methods
        #selects last country from the dropdown with last method By XPath country option/click
        #country_dropdown= driver.find_element(By.XPATH, "//select[@id='country']/option[last()]").click()
        #Select class and its methods(index and visible text)
        country_dropdown = Select(driver.find_element(By.XPATH, "//select[@id='country']"))
        #country_dropdown.select_by_index(4) #returns france
        country_dropdown.select_by_visible_text("India")

        #multiple options with scroll feature
        colors_dropdown = Select(driver.find_element(By.XPATH, "//select[@id='colors']"))
        colors_dropdown.select_by_value("white")

        #date picker by inputting the date directly in the input box
        #driver.find_element(By.XPATH, "//input[@id='datepicker']").send_keys("12/01/2023")

        #date picker by selecting the date from the picker
        driver.find_element(By.XPATH, "//input[@id='datepicker']").click()
        month = "December"
        year = '2024'
        date = '8'

        while True:
            mon = driver.find_element(By.XPATH, "//div[@class='ui-datepicker-title']/span[1]").text
            yr = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

            if month==mon and year==yr:
                break
            else:
                driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']").click()

        dates = driver.find_elements(By.XPATH, "//tr/td/a")

        for i in dates:
            if i.text == date:
                i.click()


        #open cart link
        driver.find_element(By.XPATH, "//a[normalize-space()='open cart']").click()
        driver.back()

        #web table row and column data
        rows = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr"))
        cols = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr[1]/th"))
        for row in range(2, rows+1):
            for col in range(1, cols+1):
                data = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(row)+"]/td["+str(col)+"]").text
                print(data, end='      ')
                print()

        #web table with checkbox
        # rows = len(driver.find_elements(By.XPATH, "//table[@id='productTable']//tbody/tr"))
        # cols = len(driver.find_elements(By.XPATH, "//table[@id='productTable']//tbody/tr/td"))
        # checboxes_1 = driver.find_elements(By.XPATH, "//table[@id='productTable']//tbody/tr/td[4]")
        # ID = driver.find_elements(By.XPATH, "//table[@id='productTable']//tbody/tr/td[1]")
        # #
        # # for row in range(2, rows+1):
        # #     for col in range(1, cols+1):
        # if ID==2:
        #     for i in checboxes_1:
        #         i.click()
        # time.sleep(5)

        #searchbox
        # driver.find_element(By.XPATH, "//input[@id='Wikipedia1_wikipedia-search-input']").send_keys("Drop")
        # driver.find_element(By.XPATH, "//input[@type='submit']").click()
        # search_results = driver.find_elements(By.XPATH, "//div[@id='wikipedia-search-result-link']/a")
        # for i in search_results:
        #     print(i.text)


        #Browser Window
        driver.find_element(By.XPATH, "//button[contains(.,'New Browser Window')]").click()
        windowIds = driver.window_handles
        parentWin = windowIds[0]
        childWin = windowIds[1]
        driver.switch_to.window(childWin)
        driver.switch_to.window(parentWin)
        time.sleep(3)

        #JS Alerts
        #alert1
        driver.find_element(By.XPATH, "//button[contains(text(), 'Alert')]").click()
        time.sleep(3)

        alertWindow1 = driver.switch_to.alert
        print(alertWindow1.text)
        alertWindow1.accept()


        #confirm box1
        driver.find_element(By.XPATH, "//button[text()='Confirm Box']").click()
        time.sleep(3)
        alertWindow2 = driver.switch_to.alert
        print(alertWindow2.text)
        alertWindow2.dismiss()

        #Prompt
        driver.find_element(By.XPATH, "//button[text()='Prompt']").click()
        time.sleep(3)
        alertWindow3 = driver.switch_to.alert

        print(alertWindow3.text)
        time.sleep(3)
        alertWindow3.send_keys("Hello")
        time.sleep(3)
        alertWindow3.accept()

        #DoubleClick Mouse
        Field1 = driver.find_element(By.XPATH, "//input[@id='field1']")
        Field1.clear()
        Field1.send_keys("Hello")
        CopyText = driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")
        DoubleClick = ActionChains(driver)
        DoubleClick.double_click(CopyText).perform()
        time.sleep(3)


        #DragAndDrop
        source = driver.find_element(By.XPATH, "//div[@id='draggable']/p")
        destination = driver.find_element(By.XPATH, "//div[@id='droppable']/p")

        DragAndDrop = ActionChains(driver)
        DragAndDrop.drag_and_drop(source,destination).perform()
        time.sleep(3)

        # slider
        slider = driver.find_element(By.XPATH, "//span[@class='ui-slider-handle ui-corner-all ui-state-default']")
        print("Location of slider before moving...")
        print(slider.location)
        Slide = ActionChains(driver)
        Slide.drag_and_drop_by_offset(slider,200,0).perform()
        print("Location of slider after moving...")
        print(slider.location)

        #frame
        frame = driver.find_element(By.XPATH, "(//iframe[@id='frame-one796456169'])[1]")
        driver.switch_to.frame(frame)
        #Name
        driver.find_element(By.XPATH, "//input[@id = 'RESULT_TextField-0']").send_keys("abc")
        #Gender
        driver.find_element(By.XPATH, "//label[text()='Female']").click()
        #DOB
        driver.find_element(By.XPATH,"//div[@id='q4']/input").send_keys("03/12/2023")
        #Job
        Select_Job = Select(driver.find_element(By.XPATH, "//select[@id='RESULT_RadioButton-3']"))
        Select_Job.select_by_visible_text("Automation Engineer")

        #submit
        driver.find_element(By.XPATH, "//input[@id='FSsubmit']").click()

        time.sleep(3)




Practice_Obj1 = Xpath_Practice()
Practice_Obj1.xpath()