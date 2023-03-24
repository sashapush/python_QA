#robot -d results -i smoke2  .\Tests\amazon.robot runs only specific test in file(this time by tag)
*** Settings ***
Documentation   This is some basic info about the whole suite
Resource        ../Resources/AmazonApp.robot
Resource        ../Resources/Common.robot

*** Variables ***


*** Test Cases ***
User can search for products
    [Documentation]  This is some basic info about the test
    [Tags]  Smoke
    Common.Begin web test
    AmazonApp.Search for products
    Common.End web test

User can view a product
    [Documentation]  This is some basic info about the test
    [Tags]  Smoke
    Common.Begin web test
    AmazonApp.Search for products
    AmazonApp.Select product from search results
    Common.End web test

User can add product to cart
    [Documentation]  This is some basic info about the test
    [Tags]  Smoke
    Common.Begin web test
    AmazonApp.Search for products
    AmazonApp.Select product from search results
    AmazonApp.Add product to cart
    Common.End web test

User must sign in to check out
    [Documentation]  This is some basic info about the test
    [Tags]  Smoke
    Common.Begin web test
    AmazonApp.Search for products
    AmazonApp.Select product from search results
    AmazonApp.Add product to cart
    AmazonApp.Begin checkout
    Common.End web test

