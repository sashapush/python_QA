import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_object = Service("c:\\Users\\Alex\\PycharmProjects\\autopython_scrape\\chromedriver.exe")
driver = webdriver.Chrome(service=service_object)  # expected Service object from params.
#driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#checkboxes
driver.find_element(By.NAME, "checkBoxOption2").click() #if ID/NAME is available otherwise
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']") #get the list of options and pick options with correct "value"
for ass in checkboxes:
    print(ass.get_attribute("value"))
    if ass.get_attribute("value") == "option1":
        ass.click()
        assert ass.is_selected() #will return true if selected
        break


#radiobuttons:
#rad = driver.find_elements(By.XPATH, "(//input[@type='radio'])")
rad = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
#alernatively - rad[1].click() if we are 100% sure
for r in rad:
    print(r.get_attribute("value"))
    if r.get_attribute("value") == "radio2":
        r.click()
        assert r.is_selected()
        break
#"is displayed" elements
assert driver.find_element(By.ID, "displayed-text").is_displayed() #will return true if element is displayed
driver.find_element(By.ID, "hide-textbox").click()  #we hide the element which was asserted above
assert not driver.find_element(By.ID, "displayed-text").is_displayed() #will return true if element is not displayed

#enter name and generate a browser popup
name = "Aspuppy"
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)

driver.find_element(By.ID, "alertbtn").click()

#driver.switch_to.alert.accept() # to accept the alert. Or create alert object to access its attributes
alert = driver.switch_to.alert
alerttext = alert.text
print(alerttext)
assert name in alerttext
alert.accept() # to accept, as i deducted above
#alert.dismiss() #to cancel

driver.save_screenshot("uicontrols.png")