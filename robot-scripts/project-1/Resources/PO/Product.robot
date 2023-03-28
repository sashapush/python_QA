*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${ADD_TO_CART_BUTTON} =    id=add-to-cart-button
*** Keywords ***
Verify Page Loaded
    Wait Until Page Contains        Back to results

Add to Cart
    Click Button                    ${ADD_TO_CART_BUTTON}
    Wait Until Page Contains                Added to Cart