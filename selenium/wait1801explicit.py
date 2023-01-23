import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_object = Service("c:\\Users\\Alex\\PycharmProjects\\autopython_scrape\\chromedriver.exe")
driver = webdriver.Chrome(service=service_object)  # expected Service object from params.
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(2)

disc_code = "rahulshettyacademy"
#search for specific range of products
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
products = driver.find_elements(By.XPATH, "//div[@class='products']/div")
# xpath - parent element, class name, div as a child//div[@class="products"]/div
products_count = len(products)
print(products_count)
#check that search worked correclty and "ber" exists in product name
#expected list is ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
expected_products = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
product_names = []
assert products_count == 3
for product in products:
    product_names.append(product.find_element(By.XPATH, "h4[@class='product-name']").text)  # we dig deeper to get product name for assertion; it's another chaining example; simple "h4" can also be used
    product.find_element(By.XPATH, "div/button").click()
assert expected_products == product_names
print(f"List of {product_names} is equal to {expected_products}")
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
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
assert driver.find_element(By.CLASS_NAME, "promoInfo").is_displayed()
print(driver.find_element(By.CSS_SELECTOR, ".promoInfo").text)

#to get column with the amount - we take the fifth column of the table. //td[5] xpath or //td/td[5]; td:nth-child(5) css or tr td:nth-child(5)
#and then we need to get to child add p (html tag) in css, f.e. tr td:nth-child(5) p
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
#ASSERT total price of individual products equals to "Totat amount" on page
cart_sum = 0
for item in prices:
    cart_sum += int(item.text)
print(cart_sum)
total_wo_discount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
print(total_wo_discount)
assert cart_sum == total_wo_discount
print(f"Values of sums of products {cart_sum} and Totat Amount {total_wo_discount} are equal")
#assert total value is decreased - field total value w/ discount
disc_value = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
assert disc_value < total_wo_discount
print(f"Checked that value with discount {disc_value} is less than {total_wo_discount}")
driver.save_screenshot("products_checkout.png")
#click Place order