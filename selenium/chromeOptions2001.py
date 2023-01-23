from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless") #headless #headless runs the browser in background, without UI
#chrome_options.add_argument("--ignore-certificate-errors") #skips http pages' certificate error window
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--ignore-certificate-errors")
service_object = Service("c:\\Users\\Alex\\PycharmProjects\\autopython_scrape\\chromedriver.exe")
driver = webdriver.Chrome(service=service_object, options=chrome_options) # expected Service object from params.
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)
