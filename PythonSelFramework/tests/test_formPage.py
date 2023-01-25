import pytest

from PythonSelFramework.TestData.HomePageData import HomePageData
from PythonSelFramework.pageObjects.homePage import HomePage
from PythonSelFramework.util.BaseClass import baseClass


class TestFormPage(baseClass):
    def test_formSubmission(self, userData):
        log = self.getLogger()
        log.info("Creating a HomePage object")
        homePage = HomePage(self.driver)
        # self.driver.get("https://rahulshettyacademy.com/angularpractice/" see 26 string for explanation. IF we want to use it - we need to remove this from "setup" fixture
        log.info("Typing in first name as:")
        # log.info(userData["Name"]) error
        homePage.getName().send_keys(userData["Name"])
        homePage.getEmail().send_keys(userData["Email"])
        homePage.getPassword().send_keys(userData["Password"])
        log.info("Clicking the checkbox")
        homePage.getCheckbox().click()
        homePage.getRadioButton().click()
        self.selectOptionByText(homePage.getGender(), userData["Gender"])
        homePage.getSubmitButton().click()
        homePage.getTwoWay().send_keys("Hello lol")
        homePage.getTwoWay().clear()
        message = homePage.getAlert().text
        assert "Success" in message
        print("Assert successfull")
        self.driver.refresh()
        # to refresh the browser in order to properly use test data. Alternatively - we can remove going to url from fixture of "setup" and add it as first step of this tc

    @pytest.fixture(
        params=HomePageData.test_formPage_userData)
    def userData(self, request):  # request is the param called from the list above
        return request.param
