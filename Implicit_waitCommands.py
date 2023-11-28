#implicit wait
#explicit wait
#time.sleep; advantage; simple to use, not related to selenium webdriver, but related to python; disadvantages is performance of the script is very poor, if the element is not avilable within the time mentioned, still there is a chanc of getting exception

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# implicit wait; implicit wait will be applicable for all the driver related commands for the bottom statements
# Advantages; singl implicit statement will be sufficient to handle synchronization problem in the script, performance will not be affected if the element is found within specified time as then it will go to next statement execution
# disadvantages; if the element not found there are chances of thorowing exception
driver.implicitly_wait(10)

driver.get("https://www.google.com/")
searchBox = driver.find_element(By.NAME,"q")
searchBox.send_keys("Selenium")
searchBox.submit()
driver.find_element(By.XPATH,"//a[@href='https://www.selenium.dev/']//h3[@class='LC20lb MBeuO DKV0Md'][normalize-space()='Selenium']").click()


driver.close()

