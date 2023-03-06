import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class baseClass:
    def verifyLinkPresence(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.presence_of_element_located((By.LINK_TEXT, text)))
        # or
        # WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.LINK_TEXT, text)))
        # wait.until(ec.presence_of_element_located((By.LINK_TEXT, "Belarus")))

    def save_screenshot(self, name):
        self.driver.save_screenshot(name)

    def selectOptionByText(self, locator, text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)

    def selectOptionByIndex(self, locator, index):
        dropdown = Select(locator)
        dropdown.select_by_index(index)  # selects second option (1)

    def getLogger(self):
        loggerName = inspect.stack()[1][
            3]  # improvement to properly display test_ methods in logs when using this method as inherited.
        logger = logging.getLogger(loggerName)  # __name__ catches test case name
        fileHandler = logging.FileHandler(
            "C:\\Users\\Alex\\PycharmProjects\\pythonAQAdraft\\PythonSelFramework\\util\\logs.txt")  # describe file which is used for logs
        # fileHandler = logging.FileHandler('logfile.log', mode='w') if we want to clear logs for each run
        # format of logs
        format = logging.Formatter(
            "%(asctime)s: %(levelname)s: %(name)s: %(message)s")  # example of tutor ;s is treating like a string
        fileHandler.setFormatter(format)  # adding format to file object
        if logger.hasHandlers():
            logger.handlers.clear()
        logger.addHandler(fileHandler)  # to attach logs to file, requires usage of fileHandler object
        logger.setLevel(
            logging.INFO)  # define the level of logs needed (selected is used, and below it f.e. warning = warning,error,critical
        return logger  # method will return logger (logging object)
