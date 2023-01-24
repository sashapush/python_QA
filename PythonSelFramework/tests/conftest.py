import pytest
from selenium import webdriver #fix imports
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def setup(request):
    service_object = Service("c:\\Users\\Alex\\PycharmProjects\\autopython_scrape\\chromedriver.exe")
    driver = webdriver.Chrome(service=service_object)
    driver.implicitly_wait(2)
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver#driver will be send to class object  cls - class; so class using this fixture will have access to this driver object via .driver link
    yield
    driver.close()
