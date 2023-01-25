from selenium.webdriver.common.by import By

from PythonSelFramework.pageObjects.deliveryDetails import DeliveryDetails


class Shop:
    phones_list = (By.CSS_SELECTOR, ".card.h-100")
    phone_name = (By.CSS_SELECTOR, ".card-title")
    cart_button = (By.CSS_SELECTOR, ".btn.btn-info")
    checkout_button = (By.CSS_SELECTOR, ".nav-link.btn.btn-primary")
    confirm_checkout_button = (By.XPATH, "//button[contains(text(),'Checkout')]")
    def __init__(self, driver):
        self.driver = driver

    def getPhonesList(self):
        return self.driver.find_elements(*Shop.phones_list)

    def getPhoneName(self, phone):
        return phone.find_element(*Shop.phone_name).text #we pass phone object which already had driver by chaining

    def getCartButton(self, phone):
        return phone.find_element(*Shop.cart_button) #we pass phone object which already had driver by chaining

    def getCheckoutButton(self):
        return self.driver.find_element(*Shop.checkout_button)

    def confirmCheckout(self):
        self.driver.find_element(*Shop.confirm_checkout_button).click()
        deliveryDetails = DeliveryDetails(self.driver)
        return deliveryDetails


