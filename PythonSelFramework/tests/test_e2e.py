import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from Pytest.BaseClass import BaseClass
from PythonSelFramework.pageObjects.deliveryDetails import DeliveryDetails
from PythonSelFramework.pageObjects.homePage import HomePage
from PythonSelFramework.pageObjects.shop import Shop


#we need to move browser invocation to the commonly used place, f.e. fixture
#fixture will initialise driver object and load the URL
#we need to tie fixture instance to class instance

#fixture usage should be removed from class and be a part of parent class
class TestOne(BaseClass): #inherit BaseClass to use its' fixtures
    def test_e2e_buy_phone(self, setup):
        # 1 click shop
        homePage = HomePage(self.driver)
        shopPage = homePage.shopItems()  #since we are returninh shop_page object in homePage.shopItems() method
        # 2 pass the product name to the script, f.e. click Blackberry phone from the list
        #we replaced object with shop_page above
        phones_list = shopPage.getPhonesList()
        for phone in phones_list:
            phone_name = shopPage.getPhoneName(phone)
            if phone_name == "Blackberry":
                shopPage.getCartButton(phone).click()
                # 3 add the product to cart
        # 4 checkout - checkout
        shopPage.getCheckoutButton().click()
        deliveryPage = shopPage.confirmCheckout()
        # 5 select country name and wait via explicit wait
        deliveryPage.getCountry().send_keys("Bel")
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.presence_of_element_located((By.LINK_TEXT, "Belarus")))
        deliveryPage.getSearchSuggestion().click()
        # 6 accept checkbox
        deliveryPage.getConditionsCheckbox().click()
        deliveryPage.getPurchaseButton().click()
        ass = deliveryPage.getNotification().text
        print(ass)
        # 7 assert success message
        assert "Success! Thank you!" in ass
        assert "Success! Thank you! Your order will be delivered in next few weeks :-)." in ass
        self.driver.save_screenshot("buyPhones2401.png")
