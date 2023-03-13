*** Settings ***
Documentation    This is my first attempt to robot robot, this is a suite.
Library          SeleniumLibrary    #timeout = 0:00:15
#cd .\robot-scripts\project-1
#robot -d results  .\Tests\crm.robot
#robot -d results -i 1006 .\Tests\crm.robot
#-i runs tagged cases
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
    open browser            https://automationplayground.com/crm/     edge
    maximize browser window
    #wait is more usable due to the flexibility
    wait until page contains    Customers Are Priority One!
    #or id=SignIn, SignIn (framework will find element), Sign in (as text), login.html, xpath=//*[@id="SignIn"], css=#SignIn
    click link              id=SignIn
    page should contain     Login

    input text              id=email-id     admin@robotframeworktutorial.com
    input text              id=password     qwe
    click button            id=submit-id
    wait until page contains     Our Happy Customers

    click link            id=new-customer
    wait until page contains     Add Customer


    input text              id=EmailAddress     ass@test.com
    input text              id=FirstName        Ass
    input text              id=LastName         Zopa
    input text              id=City             Ass-city
    select from list by value    id=StateOrRegion     AZ
    select radio button    gender      female
    select checkbox    promos-name
    click button    Submit
    wait until page contains     Success! New customer added.


    sleep                   5
    close browser


*** Keywords ***


#https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html#Open%20Browser documentation