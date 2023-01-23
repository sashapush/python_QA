import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_object = Service("c:\\Users\\Alex\\PycharmProjects\\autopython_scrape\\chromedriver.exe")
driver = webdriver.Chrome(service=service_object)  # expected Service object from params.
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(5)

disc_code = "rahulshettyacademy"
#search for specific range of products
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
products = driver.find_elements(By.XPATH, "//div[@class='products']/div")
# xpath - parent element, class name, div as a child//div[@class="products"]/div
products_count = len(products)
print(products_count)
assert products_count == 3
for product in products:
    product.find_element(By.XPATH, "div/button").click()
# xpath - parent element, class name, div as a child//div[@class="products"]/div/div/button as a whole. But due to
# *chaining* we can add the remaining xpath needed to the already added one


#time.sleep(2)

#next we click on cart and proceed to checkout
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
#time.sleep(1)
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click() #click "Proceed to checkout button"
#apply and assert discount element
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys(disc_code)
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
assert driver.find_element(By.CLASS_NAME, "promoInfo").is_displayed()
print(driver.find_element(By.CSS_SELECTOR, ".promoInfo").text)


driver.save_screenshot("products_checkout.png")

#assert total value is decreased - field total value w/ discount
#assert total price of individual products equals to "Totat amount" on page
#click Place order