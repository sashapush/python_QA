#cd .\robot-scripts\project-1\
#robot -d results -i smoke2  .\Tests\amazon.robot runs only specific test in file(this time by tag)
#robot -d results .\Tests\amazon.robot
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
*** Test Cases ***
User can search for products
    [Documentation]  This is some basic info about the test
    [Tags]  Smoke
    AmazonApp.Search for products

User can view a product
    [Documentation]  This is some basic info about the test
    [Tags]  Smoke
    AmazonApp.Search for products
    AmazonApp.Select product from search results

User can add product to cart
    [Documentation]  This is some basic info about the test
    [Tags]  Smoke
    AmazonApp.Search for products
    AmazonApp.Select product from search results
    AmazonApp.Add product to cart

User must sign in to check out
    [Documentation]  This is some basic info about the test
    [Tags]  Smoke
    AmazonApp.Search for products
    AmazonApp.Select product from search results
    AmazonApp.Add product to cart
    AmazonApp.Begin checkout

