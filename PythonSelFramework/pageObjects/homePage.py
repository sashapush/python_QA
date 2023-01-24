from selenium.webdriver.common.by import By

class HomePage:
    shop_link = (By.CSS_SELECTOR, ".nav-link[href='/angularpractice/shop']")

    def __init__(self, driver):
        self.driver = driver

    def shopItems(self):
         return self.driver.find_element(*HomePage.shop_link) #* is used to let python know that it's a tuple and that it should be parsed as tuple
         #self.driver since we need to access instance variable, from the constructor above.
         # above equals to  self.driver.find_element(By.CSS_SELECTOR, ".nav-link[href='/angularpractice/shop']") from test_e2e.py
        #driver should come from actual test case - that's why we create constructor

