from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

#service_object = Service("C:\\Users\\Alex\\PycharmProjects\\autopython_scrape\\geckodriver.exe")
driver = webdriver.Firefox()  # expected Service object from params.
driver.implicitly_wait(2)
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()
l = driver.window_handles
print(l)
driver.switch_to.window(l[1])
text = driver.find_element(By.TAG_NAME, "h3").text
print(text)
driver.switch_to.window(l[0])
text = driver.find_element(By.TAG_NAME, "h3").text
print(text)
assert text == "Opening a new window"
#driver.close() #closes child tab
driver.stop_client()
