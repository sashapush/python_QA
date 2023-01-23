from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.firefox.service import Service

# demo of webdriver, chrome. We need to call driver with .exe file
#Chrome
#service_object = Service("c:\\Users\\Alex\\PycharmProjects\\autopython_scrape\\chromedriver.exe")
#driver = webdriver.Chrome(service=service_object)  # expected Service object from params.

#Firefox
service_object = Service("c:\\Users\\Alex\\PycharmProjects\\autopython_scrape\\geckodriver.exe")
driver = webdriver.Firefox()#service=service_object)  # expected Service object from params.

#Edge
#service_object = Service("c:\\Users\\Alex\\PycharmProjects\\autopython_scrape\\msedgedriver.exe")
#driver = webdriver.Edge(service=service_object)  # expected Service object from params.

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)
print(driver.current_url)
driver.find_element(by="xpath", value="/html/body/app-root/form-comp/div/form/div[2]/input").send_keys("TestVasyan@gmail.com")
driver.save_screenshot("xpath.png")
#driver.get("https://amiami.com")
#driver.back()
#driver.forward()
#print(driver.current_url)
#driver.refresh()
#driver.implicitly_wait(10) to investigate
#driver.minimize_window()
driver.close() #to close driver