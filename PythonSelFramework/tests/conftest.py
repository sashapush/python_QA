import pytest
from selenium import webdriver #fix imports
from selenium.webdriver.chrome.service import Service

#tell pytest that there are going to be new command-line arguments and we need to parse them see
#https://docs.pytest.org/en/latest/example/simple.html
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="acceptable options - chrome, firefox, edge",  choices=("chrome", "firefox", "edge")
    )
@pytest.fixture(scope="class")
def setup(request):
    #to retrieve command line argumet --browser_name
    browser_name = request.config.getoption("browser_name")
    print(browser_name)
    if browser_name == "chrome":
        service_object = Service("c:\\Users\\Alex\\PycharmProjects\\autopython_scrape\\chromedriver.exe")
        driver = webdriver.Chrome(service=service_object)
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "edge":
        service_object = Service("c:\\Users\\Alex\\PycharmProjects\\autopython_scrape\\msedgedriver.exe")
        driver = webdriver.Edge(service=service_object)  # expected Service object from params.
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.implicitly_wait(2)
    driver.maximize_window()
    request.cls.driver = driver#driver will be send to class object  cls - class; so class using this fixture will have access to this driver object via .driver link
    yield
    driver.close()

