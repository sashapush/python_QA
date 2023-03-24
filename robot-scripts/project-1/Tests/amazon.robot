#robot -d results -i smoke2  .\Tests\amazon.robot runs only specific test in file(this time by tag)
*** Settings ***
Documentation   This is some basic info about the whole suite
Library         SeleniumLibrary

*** Variables ***


*** Test Cases ***
User can search for products
    [Documentation]  This is some basic info about the test
    [Tags]  Smoke
    Begin web test
    Search for products
    End web test

User can view a product
    [Documentation]  This is some basic info about the test
    [Tags]  Smoke
    Begin web test
    Search for products
    Select product from search results
    Close Browser

User can add product to cart
    [Documentation]  This is some basic info about the test
    [Tags]  Smoke
    Begin web test
    Search for products
    Select product from search results
    Add product to cart
    Close Browser

User must sign in to check out
    [Documentation]  This is some basic info about the test
    [Tags]  Smoke
    Begin web test
    Search for products
    Select product from search results
    Add product to cart
    Begin checkout
    End web test

*** Keywords ***
Begin web test
    Open Browser                            about:blank       chrome
    Maximize Browser Window
Search for products
    Go To                                   http://www.amazon.com
    Wait Until Page Contains                Search Amazon
    Input Text                              id=twotabsearchtextbox      Ferrari 458
    Click Button                            xpath=//*[@id="nav-search-submit-button"]
    Wait Until Page Contains                results for "Ferrari 458"
Select product from search results
    Wait Until Element Is Visible           xpath=//span[normalize-space()='Bburago B18-26017 1:24 Scale Race and Play of The Ferrari 458 Spider Sports Car Die-Cast Model']
    Click Link                              css=div[class='s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_1'] a[class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']
    Wait Until Page Contains                Back to results
Add product to cart
    Click Button                            id=add-to-cart-button
    Wait Until Page Contains                Added to Cart
#if anything opens in new tab - move control to it via "SELECT Window NEW "
Begin checkout
    Wait Until Page Contains                Proceed to checkout
    Click Element                           css=input[aria-labelledby='attach-sidesheet-checkout-button-announce']
    Page Should Contain Element             css=h1[class='a-spacing-small']
    Element Text Should Be                  css=h1[class='a-spacing-small']    Sign in

End web test
    Close Browser