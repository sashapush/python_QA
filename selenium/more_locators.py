import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.firefox.service import Service
# demo of webdriver, chrome. We need to call driver with .exe file
# Chrome
service_object = Service("c:\\Users\\Alex\\PycharmProjects\\autopython_scrape\\chromedriver.exe")
driver = webdriver.Chrome(service=service_object)  # expected Service object from params.

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/client/")
print(driver.title)
print(driver.current_url)
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
#xpath element via html tags //form/div[1]/input = email field
#xpath of the password field //form/div[2]/input ; xpath of the password label //form/div[2]/label
#//input[@formcontrolname='userPassword']
#css of the password field form div:nth-child(2) input ; xpath of the password label //form/div[2]/label
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("password")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("password") #css locators are faster
#xpath by text //button[text()="Save New Password"]
driver.find_element(By.XPATH, "//button[@type='submit']").click()

driver.save_screenshot("forgot_password_form.png")
time.sleep(10)



