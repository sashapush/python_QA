from selenium.webdriver.common.by import By


class DeliveryDetails:

    country = (By.ID, "country")
    search_suggestion = (By.LINK_TEXT, "Belarus")
    conditions_checkbox = (By.CSS_SELECTOR, ".checkbox.checkbox-primary")
    purchase_button = (By.XPATH, "//input[@value='Purchase']")
    notification = (By.CSS_SELECTOR,".alert.alert-success.alert-dismissible")
    def __init__(self, driver):
        self.driver = driver

    def getCountry(self):
        return self.driver.find_element(*DeliveryDetails.country)

    def getSearchSuggestion(self):
        return self.driver.find_element(*DeliveryDetails.search_suggestion)

    def getConditionsCheckbox(self):
        return self.driver.find_element(*DeliveryDetails.conditions_checkbox)

    def getPurchaseButton(self):
        return self.driver.find_element(*DeliveryDetails.purchase_button)

    def getNotification(self):
        return self.driver.find_element(*DeliveryDetails.notification)
