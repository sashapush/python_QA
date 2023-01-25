from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PythonSelFramework.pageObjects.homePage import HomePage
from PythonSelFramework.util.BaseClass import baseClass


class TestFormPage(baseClass):
    def test_formSubmission(self):
        homePage = HomePage(self.driver)
        homePage.getName().send_keys("John Cena")
        homePage.getEmail().send_keys("TestVasyan@gmail.com")
        homePage.getPassword().send_keys("Ololololo")
        homePage.getCheckbox().click()
        homePage.getRadioButton().click()
        dropdown = Select(homePage.getDropdown())
        dropdown.select_by_index(1)  # selects second option
        dropdown.select_by_visible_text("Male")  # selects option based on visible text
        homePage.getSubmitButton().click()
        homePage.getTwoWay().send_keys("Hello lol")
        homePage.getTwoWay().clear()
        message = homePage.getAlert()
        self.save_screenshot("localtors_refactored.png")
        assert "Success" in message

