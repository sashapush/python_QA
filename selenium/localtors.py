import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# from selenium.webdriver.firefox.service import Service

# demo of webdriver, chrome. We need to call driver with .exe file
# Chrome
service_object = Service("c:\\Users\\Alex\\PycharmProjects\\autopython_scrape\\chromedriver.exe")
driver = webdriver.Chrome(service=service_object)  # expected Service object from params.

# Firefox
# service_object = Service("c:\\Users\\Alex\\PycharmProjects\\autopython_scrape\\geckodriver.exe")
# driver = webdriver.Firefox()#service=service_object)  # expected Service object from params.

# Edge
# service_object = Service("c:\\Users\\Alex\\PycharmProjects\\autopython_scrape\\msedgedriver.exe")
# driver = webdriver.Edge(service=service_object)  # expected Service object from params.


driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)
print(driver.current_url)

# Locators could be one of the following - id,xpath,cssselector,classname,name,linktext
driver.find_element(by="xpath", value="/html/body/app-root/form-comp/div/form/div[2]/input").send_keys(
    "TestVasyan@gmail.com")
# or
driver.find_element(By.NAME, "email").send_keys("Ololololo")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("Ololololo")
driver.find_element(By.ID, "exampleCheck1").click()

# css locators are like
# alternatively #id .classname
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Igor")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()

#Static dropdown
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
print(type(dropdown))
print(dropdown)
dropdown.select_by_index(1) #selects second option
dropdown.select_by_visible_text("Male") #selects option based on visible text
#dropdown.select_by_value("Female") #selects option based on <value> tag
# xpath:
# //tagname[@attribute='value'] -> f.e. //input[@type='submit']
driver.find_element(by="xpath", value="//input[@type='submit']").click()
driver.find_element(By.XPATH, value="(//input[@type='text'])[3]").send_keys(
    "Hello lol")  # third text field from the top
driver.find_element(By.XPATH, value="(//input[@type='text'])[3]").clear()  # to empty the field
message = driver.find_element(By.CLASS_NAME, "alert-success").text

driver.save_screenshot("example.png")
# driver.close() #to close driver
# time.sleep(10)
assert "Success" in message
