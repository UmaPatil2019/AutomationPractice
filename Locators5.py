from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class Locators5_demo():
    def Locators5(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
        #self-node
        self_node=driver.find_element(By.XPATH,"//a[contains(text(),'Nesco Ltd.')]/self::a").text
        print("self node;", self_node)
        time.sleep(3)
        #parent-node
        parent_node=driver.find_element(By.XPATH, "//a[contains(text(),'Nesco Ltd.')]/parent::td").text
        print("parent node;", parent_node)
        # time.sleep(3)
        # #child-node
        child_nodes = driver.find_elements(By.XPATH, "//a[contains(text(),'Nesco Ltd.')]/ancestor::tr/child::td")
        time.sleep(3)
        print(len(child_nodes))
        for i in child_nodes:
            print("child nodes: " + i.text)
        # #ancestor-node
        ancestor_nodes = driver.find_element(By.XPATH,"//a[contains(.,'Nesco Ltd.')]/ancestor::tr").text
        time.sleep(3)
        print("ancestor_nodes: " + ancestor_nodes)
        # #descendent-node
        descendant_nodes = driver.find_elements(By.XPATH,"//a[contains(.,'Nesco Ltd.')]/ancestor::tr/descendant::td")
        time.sleep(3)
        print(len(descendant_nodes))
        for i in descendant_nodes:
            print("descendant nodes: " + i.text)
        # #following-nodes
        following_nodes = driver.find_elements(By.XPATH, "//a[contains(.,'Nesco Ltd.')]/ancestor::tr/following::*")
        time.sleep(3)
        print("following nodes",len(following_nodes))
        #following-siblings
        following_siblings = driver.find_elements(By.XPATH,"//a[contains(.,'Nesco Ltd.')]/ancestor::tr/following-sibling::*")
        print("following siblings", len(following_siblings))
        # #preceding
        preceding= driver.find_elements(By.XPATH, "//a[contains(.,'Nesco Ltd.')]/ancestor::tr/preceding::*")
        print("all preceding nodes", len(preceding))
        # #preceding-siblings
        preceding_siblings = driver.find_elements(By.XPATH, "//a[contains(.,'Nesco Ltd.')]/ancestor::tr/preceding-sibling::tr")
        print("preceding siblings",len(preceding_siblings))

        driver.close()
obj5 = Locators5_demo()
obj5.Locators5()

