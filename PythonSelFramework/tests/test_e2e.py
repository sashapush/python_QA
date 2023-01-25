from PythonSelFramework.util.BaseClass import baseClass
from PythonSelFramework.pageObjects.homePage import HomePage

class TestOne(baseClass): #inherit BaseClass to use its' fixtures
    def test_e2e_buy_phone(self, setup):
        log = self.getLogger()
        log.info("HomePage object created")
        # 1 click shop
        homePage = HomePage(self.driver)
        shopPage = homePage.shopItems()  # since we are returninh shop_page object in homePage.shopItems() method
        # 2 pass the product name to the script, f.e. click Blackberry phone from the list
        # we replaced object with shop_page above
        log.info("Getting phone list")
        phones_list = shopPage.getPhonesList()
        for phone in phones_list:
            phone_name = shopPage.getPhoneName(phone)
            log.info(phone_name)
            if phone_name == "Blackberry":
                shopPage.getCartButton(phone).click()
                # 3 add the product to cart
        # 4 checkout - checkout
        log.info("Going to delivery details page")
        shopPage.getCheckoutButton().click()
        deliveryPage = shopPage.confirmCheckout()
        # 5 select country name and wait via explicit wait
        deliveryPage.getCountry().send_keys("Bel")
        #self.getLogger() to update with proper base class
        self.verifyLinkPresence("Belarus")
        deliveryPage.getSearchSuggestion().click()
        # 6 accept checkbox
        deliveryPage.getConditionsCheckbox().click()
        deliveryPage.getPurchaseButton().click()
        ass = deliveryPage.getNotification().text
        log.info("Text parsed is: " + ass)
        # 7 assert success message
        assert "Success! Thank you!" in ass
        assert "Success! Thank you! Your order will be delivered in next few weeks :-)." in ass
        self.driver.save_screenshot("buyPhones2501.png")
