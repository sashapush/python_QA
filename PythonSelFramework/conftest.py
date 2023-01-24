import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service

#t
@pytest.fixture(scope="class")
def setup():
    service_object = Service("c:\\Users\\Alex\\PycharmProjects\\autopython_scrape\\chromedriver.exe")
    driver = webdriver.Chrome(service=service_object)
    driver.implicitly_wait(2)
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    return driver