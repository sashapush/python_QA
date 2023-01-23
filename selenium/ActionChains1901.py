import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_object = Service("c:\\Users\\Alex\\PycharmProjects\\autopython_scrape\\chromedriver.exe")
driver = webdriver.Chrome(service=service_object)  # expected Service object from params.
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#ActionChains allows for mouse hover
actions = ActionChains(driver)
#actions.click_and_hold().perform()
#actions.context_click().perform() right click
#actions.drag_and_drop().perform()
actions.move_to_element(driver.find_element(By.CSS_SELECTOR, "#mousehover")).perform()
#actions.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
driver.save_screenshot("ActionChains.png")
#driver.find_element(By.LINK_TEXT, "Reload").click() or
actions.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()
driver.close()
