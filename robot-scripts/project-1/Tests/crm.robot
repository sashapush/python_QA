*** Settings ***
Documentation    This is my first attempt to robot robot, this is a suite.
Library          SeleniumLibrary    timeout = 0:00:15

#timeout is set globally this way. Can be done more precisely

*** Variables ***


*** Test Cases ***
Should be able to add new customer
    [Documentation]    Infromtatiopn abpiut this specific test
    [Tags]             1006   Contacts    Smoke
    Log                Starting the test case (info message)
    OPEN BROWSER       https://automationplayground.com/crm/     chrome
    sleep              5
    close browser


*** Keywords ***


#https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html#Open%20Browser documentation