#cd .\robot-scripts\project-1\
#robot -d results -i smoke2  .\Tests\amazon.robot runs only specific test in file(this time by tag)
#robot -d results .\Tests\amazon.robot
#Example of variables being used from Command line
#robot -v BROWSER:Chrome -d results .\Tests\amazon.robot
*** Settings ***
Documentation   This is some basic info about the whole suite
Resource        ../Resources/AmazonApp.robot
Resource        ../Resources/Common.robot

Suite Setup    Common.Generate test data
Test Setup    Common.Begin web test
Test Teardown  Common.End web test
Suite Teardown    Common.Remove test data
#Suite Setup - run before all testcases
#Suite teardown - run after all testcases
*** Variables ***
${BROWSER} =    edge
${START_URL} =    https://amazon.com
${SEARCH_TERM} =  Ferrari 458
${LOGIN_EMAIL} =    1234@test.com
${LOGIN_PASSWORD} =    testpassword

*** Test Cases ***
Should be able to login
    [Documentation]  New test
    [Tags]  Sand
    AmazonApp.Login     ${LOGIN_EMAIL}     ${LOGIN_PASSWORD}

Should not be able to login with invalid credentials
    [Documentation]  New test
    [Tags]  Sand
    SignIn.Fill "Email" Field      test@teet
    SignIn.Fill "Password" Field    1231232
    SignIn.Click "Submit" Button

Logged out user should be able to search for products
    [Documentation]  This is some basic info about the test
    [Tags]  Smoke
    AmazonApp.Search for products

Logged out user should be able to view a product
    [Documentation]  This is some basic info about the test
    [Tags]  Smoke
    AmazonApp.Search for products
    AmazonApp.Select product from search results

Logged out user should be able to add product to cart
    [Documentation]  This is some basic info about the test
    [Tags]  Smoke
    AmazonApp.Search for products
    AmazonApp.Select product from search results
    AmazonApp.Add product to cart

Logged out user should be asked to sign in to check out
    [Documentation]  This is some basic info about the test
    [Tags]  Smoke2
    AmazonApp.Search for products
    AmazonApp.Select product from search results
    AmazonApp.Add product to cart
    AmazonApp.Begin checkout

