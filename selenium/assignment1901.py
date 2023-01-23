from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

#goal is to go https://rahulshettyacademy.com/loginpagePractise/
#click top right link, store "Please email us at mentor@rahulshettyacademy.com with below template to receive response"
#and parse this, get email and put email to /loginpagePractise/ put any password and click sign in button
#get the error message and print it

service_object = Service("c:\\Users\\Alex\\PycharmProjects\\autopython_scrape\\chromedriver.exe")
driver = webdriver.Chrome(service=service_object)  # expected Service object from params.
driver.implicitly_wait(4)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.CSS_SELECTOR, ".blinkingText").click() #.class
windows = driver.window_handles
driver.switch_to.window(windows[1])
text = driver.find_element(By.CSS_SELECTOR, ".im-para.red").text
#x = text.split() correct way to split at the exact word
#email = x[4]

#or the same in one go:
#x = text.split("at")[1]
#x = x.strip()
#x = x.split(" ")[0]
x = text.split("at")[1].strip().split(" ")[0]
#OR  for element in emailAddress.split(" "):
        #if element.__contains__("@"):
        #    emailAddress = element
        #    break


print(x)
driver.switch_to.window(windows[0])
driver.find_element(By.CSS_SELECTOR, "#username").send_keys(email)

driver.find_element(By.CSS_SELECTOR, "#password").send_keys("incorrect password")
driver.find_element(By.CSS_SELECTOR, ".btn.btn-info.btn-md").click()
wait = WebDriverWait(driver, 5)
#wait.until(ec.element_attribute_to_include((By.CSS_SELECTOR, ".alert.alert-danger.col-md-12"), "style=display: block;"))
wait.until(ec.visibility_of(driver.find_element(By.CSS_SELECTOR, ".alert.alert-danger.col-md-12")))
error_text = driver.find_element(By.CSS_SELECTOR, ".alert.alert-danger.col-md-12").text
print(error_text)
driver.save_screenshot("assignment1901.png")
