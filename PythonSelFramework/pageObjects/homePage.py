from selenium.webdriver.common.by import By

from PythonSelFramework.pageObjects.shop import Shop


class HomePage:
    shop_link = (By.CSS_SELECTOR, ".nav-link[href='/angularpractice/shop']")
    name_field = (By.XPATH, "//input[@name='name']")
    # driver.find_element(By.CSS_SELECTOR, "input[name='name']") #takes first element, but there are 2
    email_field = (By.NAME, "email")
    password_field = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    radio_button = (By.CSS_SELECTOR, "#inlineRadio1")
    dropdown = (By.ID, "exampleFormControlSelect1")
    submit_button = (By.XPATH, "//input[@type='submit']")
    two_way_data = (By.XPATH, "(//input[@type='text'])[3]")
    alert = (By.CLASS_NAME, "alert-success")
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

    def getName(self):
        return self.driver.find_element(*HomePage.name_field)
    def getEmail(self):
        return self.driver.find_element(*HomePage.email_field)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password_field)
    def getCheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)
    def getRadioButton(self):
        return self.driver.find_element(*HomePage.radio_button)

    def getGender(self):
        return self.driver.find_element(*HomePage.dropdown)

    def getSubmitButton(self):
        return self.driver.find_element(*HomePage.submit_button)
    def getTwoWay(self):
        return self.driver.find_element(*HomePage.two_way_data)
    def getAlert(self):
        return self.driver.find_element(*HomePage.alert)
