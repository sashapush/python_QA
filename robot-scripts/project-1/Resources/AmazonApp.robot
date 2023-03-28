*** Settings ***
Library         SeleniumLibrary
Resource        ../Resources/PO/LandingPage.robot
Resource        ../Resources/PO/Cart.robot
Resource        ../Resources/PO/SignIn.robot
Resource        ../Resources/PO/TopNav.robot
*** Keywords ***
Search for products
    LandingPage.Load
    LandingPage.Verify Page Loaded
    TopNav.Search For Products
    Wait Until Page Contains                results for "${SEARCH_TERM}"
Select product from search results
    Wait Until Element Is Visible           xpath=//span[normalize-space()='Bburago B18-26017 1:24 Scale Race and Play of The Ferrari 458 Spider Sports Car Die-Cast Model']
    Click Link                              css=div[class='s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_1'] a[class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']
    Wait Until Page Contains                Back to results
Add product to cart
    Click Button                            id=add-to-cart-button
    Wait Until Page Contains                Added to Cart
#if anything opens in new tab - move control to it via "SELECT Window NEW "
Begin checkout
    Cart.Proceed to checkout
    SignIn.Verify Page Loaded

