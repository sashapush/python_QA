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
        # wait.until(ec.presence_of_element_located((By.LINK_TEXT, "Belarus")))

    def save_screenshot(self, name):
        self.driver.save_screenshot(name)

    def selectOptionByText(self, locator, text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)

    def selectOptionByIndex(self, locator, index):
        dropdown = Select(locator)
        dropdown.select_by_index(index)  # selects second option (1)
