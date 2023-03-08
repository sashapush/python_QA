*** Settings ***
Documentation    This is my first attempt to robot robot, this is a suite.
Library          SeleniumLibrary    #timeout = 0:00:15
#cd .\robot-scripts\project-1
#robot -d results  .\Tests\crm.robot

#timeout is set globally this way. Can be done more precisely

*** Variables ***


*** Test Cases ***
Should be able to add new customer
    [Documentation]         Information about this specific test
    #tags will allow us to run specific tests
    [Tags]                  1006   Contacts    Smoke
    #Comment to selenium initialisation
    Set Selenium Speed         .2
    Set Selenium Timeout    5

    log                     Starting the test case (info message)
    #open browser in maximized
    open browser            https://automationplayground.com/crm/     ff
    maximize browser window
    sleep                   5
    close browser


*** Keywords ***


#https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html#Open%20Browser documentation