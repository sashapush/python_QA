import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_object = Service("c:\\Users\\Alex\\PycharmProjects\\autopython_scrape\\chromedriver.exe")
driver = webdriver.Chrome(service=service_object)  # expected Service object from params.
#driver.maximize_window()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID, "autosuggest").send_keys("ame")
driver.execute_script('el = document.elementFromPoint(0, 10); el.click();') #random click
#driver.find_element(By.ID, "autosuggest").send_keys("british")
time.sleep(2)
#css locator for dropdown "li[class='ui-menu-item'] a"
countriesass = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a") #find_elements! looks for several elements
#print(len(countriesass)) #checks the length of the list (3)
for country in countriesass:
    print(country.text)
    #if country.text == "American Samoa": #TODO not working with American Samoa.
    #if country.text == "British Indian Ocean Territory":
    if country.text == "Cameroon":
        country.click()
        break #once the desired country is clicked
driver.save_screenshot("cameroon.png")
print(driver.find_element(By.ID, "autosuggest").text)
print("printing value" + driver.find_element(By.ID, "autosuggest").get_property("value"))  #can access dynamically entered values, unlike .text
assert driver.find_element(By.ID, "autosuggest").get_property("value") == "Cameroon"