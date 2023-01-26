import os
from datetime import datetime

import pytest
from selenium import webdriver  # fix imports
from selenium.webdriver.chrome.service import Service

# tell pytest that there are going to be new command-line arguments and we need to parse them see
# https://docs.pytest.org/en/latest/example/simple.html


driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="acceptable options - chrome, firefox, edge",
        choices=("chrome", "firefox", "edge")
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver  # global variable allows to update variable out of fixture

    # to retrieve command line argumet --browser_name
    browser_name = request.config.getoption("browser_name")
    print(browser_name)
    if browser_name == "chrome":
        service_object = Service("c:\\Users\\Alex\\PycharmProjects\\autopython_scrape\\chromedriver.exe")
        driver = webdriver.Chrome(service=service_object)
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "edge":
        service_object = Service("d:\\tools\\msedgedriver.exe")
        driver = webdriver.Edge(service=service_object)  # expected Service object from params.
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.implicitly_wait(2)
    driver.maximize_window()
    request.cls.driver = driver  # driver will be send to class object  cls - class; so class using this fixture will have access to this driver object via .driver link
    yield
    driver.close()


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    if not os.path.exists("C:\\Users\\lera\\PycharmProjects\\python_QA\\PythonSelFramework\\reports\\"):
        os.makedirs("C:\\Users\\lera\\PycharmProjects\\python_QA\\PythonSelFramework\\reports\\")
    config.option.htmlpath = (
            datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".html"
    )


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" or report.when == "setup":

        xfail = hasattr(report, "wasxfail")

        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = (
                        '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" '
                        'onclick="window.open(this.src)" align="right"/></div>' %file_name
                )
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
