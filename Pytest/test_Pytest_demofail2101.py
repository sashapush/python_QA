import pytest


@pytest.mark.smoke
def test_failDemo(setup):
    assert 2 == 3


@pytest.mark.smoke
@pytest.mark.xfail
def test_pass(setup):
    a = 2
    b = 4
    assert a + 2 == b, "Sum is not correct"


@pytest.mark.regression
def test_phone():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as ec
    from selenium.webdriver.support.wait import WebDriverWait

    service_object = Service("c:\\Users\\Alex\\PycharmProjects\\autopython_scrape\\chromedriver.exe")
    driver = webdriver.Chrome(service=service_object)
    driver.implicitly_wait(2)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
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
    # assert ass == "Success! Thank you! Your order will be delivered in next few weeks :-)."
    driver.save_screenshot("buyPhones2001.png")
    driver.close()
