from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("headless") #headless runs the browser in background, without browser's UI
#chrome_options.add_argument("--ignore-certificate-errors") #skips http pages' certificate error window
service_object = Service("c:\\Users\\Alex\\PycharmProjects\\autopython_scrape\\chromedriver.exe")
driver = webdriver.Chrome(service=service_object)#, options=chrome_options)  # expected Service object from params.
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
#click on column header to sort
driver.find_element(By.CSS_SELECTOR, "tr:first-child th:first-child").click()
#collect all products names - list sorted by browser
l = driver.find_elements(By.CSS_SELECTOR, "tr td:first-child") #css tr td:first-child     xpath //tr/td[1]
veggies = []
for item in l:
    veggies.append(item.text)
print(veggies)
#pre-sorted list is collected separately
web_sorted_list = veggies.copy()

#sort the list via code => new_sorted_list= list.sort()
veggies.sort()
#veggies.sort(reverse=True)
print(veggies)

#assert list==new_sorted_list -goal is to check if a WEB sorting is bugged
assert veggies == web_sorted_list
print("Sorting has been successfull")





driver.save_screenshot("sorting1901.png")
