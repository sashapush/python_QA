from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless") #headless #headless runs the browser in background, without UI
#chrome_options.add_argument("--ignore-certificate-errors") #skips http pages' certificate error window
service_object = Service("c:\\Users\\Alex\\PycharmProjects\\autopython_scrape\\chromedriver.exe")
driver = webdriver.Chrome(service=service_object, options=chrome_options)  # expected Service object from params.



driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#js code to scroll to the page bottom window.scrollTo(0,document.body.scrollHeight)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#alternate way to take screenshot is
driver.get_screenshot_as_file("misc1901(1).png")
driver.save_screenshot("misc1901.png")
print("Success")
