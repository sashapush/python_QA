from selenium.webdriver.common.by import By

from PythonSelFramework.pageObjects.shop import Shop


class HomePage:
    shop_link = (By.CSS_SELECTOR, ".nav-link[href='/angularpractice/shop']")

    def __init__(self, driver):
        self.driver = driver

    def shopItems(self):
         self.driver.find_element(*HomePage.shop_link).click()
         shopPage = Shop(self.driver) #we create object of another page in method which sends us to this another page
         return shopPage #we return the object to let python use it in test
         #* is used to let python know that it's a tuple and that it should be parsed as tuple
         #self.driver since we need to access instance variable, from the constructor above.
         # above equals to  self.driver.find_element(By.CSS_SELECTOR, ".nav-link[href='/angularpractice/shop']") from test_e2e.py
        #driver should come from actual test case - that's why we create constructor

