*** Settings ***
Library         SeleniumLibrary
Resource        ../Resources/PO/LandingPage.robot
Resource        ../Resources/PO/Cart.robot
Resource        ../Resources/PO/SignIn.robot
Resource        ../Resources/PO/TopNav.robot
Resource        ../Resources/PO/Product.robot
Resource        ../Resources/PO/SearchResults.robot

*** Keywords ***
Login
    [Arguments]     ${Username}    ${Password}
    SignIn.Login With Valid Credentials    ${Username}    ${Password}
Search for products
    LandingPage.Load
    LandingPage.Verify Page Loaded
    TopNav.Search For Products
    SearchResults.Verify Search Completed

Select product from search results
    SearchResults.Click Product Link
    Product.Verify Page Loaded

Add product to cart
    Product.Add To Cart
#if anything opens in new tab - move control to it via "SELECT Window NEW "

Begin checkout
    Cart.Proceed to checkout
    SignIn.Verify Page Loaded

