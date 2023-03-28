*** Settings ***
Library  SeleniumLibrary
*** Variables ***

*** Keywords ***
Proceed to checkout
    Wait Until Page Contains                Proceed to checkout
    Click Element                           css=input[aria-labelledby='attach-sidesheet-checkout-button-announce']