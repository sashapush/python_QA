import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

#we need to move browser invocation to the commonly used place, f.e. fixture
#fixture will initialise driver object and load the URL
#to use the fixture across class TestOne - use the string below
@pytest.mark.usefixtures("setup")
class TestOne:
    def test_e2e_buy_phone(self):


        # 1 click shop
        driver.find_element(By.CSS_SELECTOR, ".nav-link[href='/angularpractice/shop']").click()
        # alternative css locator = a[href*='shop'] a is tag, href* searches for value with wildcart
        # 2 pass the product name to the script, f.e. click Blackberry phone from the list
        phones_list = driver.find_elements(By.CSS_SELECTOR,
                                           ".card.h-100")  # alt css ".card-body" ".col-lg-3.col-md-6.mb-3" xpath //div[@class="card h-100"]
        for phone in phones_list:
            if phone.find_element(By.CSS_SELECTOR, ".card-title").text == "Blackberry":
                # 3 add the product to cart
                phone.find_element(By.CSS_SELECTOR, ".btn.btn-info").click()
        # 4 checkout - checkout
        driver.find_element(By.CSS_SELECTOR,
                            ".nav-link.btn.btn-primary").click()  # or use xpath //a[contains(text(),'Checkout')]
        driver.find_element(By.XPATH,
                            "//button[contains(text(),'Checkout')]").click()  # or use xpath //a[contains(text(),'Checkout')]#
        # 5 select country name and wait via explicit wait
        driver.find_element(By.ID, "country").send_keys("Bel")
        wait = WebDriverWait(driver, 10)
        wait.until(ec.presence_of_element_located((By.LINK_TEXT, "Belarus")))
        driver.find_element(By.LINK_TEXT, "Belarus").click()
        # 6 accept checkbox
        driver.find_element(By.CSS_SELECTOR, ".checkbox.checkbox-primary").click()
        driver.find_element(By.XPATH, "//input[@value='Purchase']").click()
        ass = driver.find_element(By.CSS_SELECTOR,
                                  ".alert.alert-success.alert-dismissible").text  # one class can be used as well
        print(ass)
        # 7 assert success message
        assert "Success! Thank you!" in ass
        assert "Success! Thank you! Your order will be delivered in next few weeks :-)." in ass
        driver.save_screenshot("buyPhones2001.png")
        driver.close()
