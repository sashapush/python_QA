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
        self.selectOptionByText(homePage.getGender(), "Male")
        # or by index (text should be better)
        self.selectOptionByIndex(homePage.getGender(), 1)
        homePage.getSubmitButton().click()
        homePage.getTwoWay().send_keys("Hello lol")
        homePage.getTwoWay().clear()
        message = homePage.getAlert().text
        self.save_screenshot("localtors_refactored.png")
        assert "Success" in message
        print("Assert successfull")
