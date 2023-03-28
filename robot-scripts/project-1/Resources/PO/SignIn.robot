*** Settings ***
Library  SeleniumLibrary
*** Variables ***
${SIGNIN_MAIN_HEADING} =    css=h1[class='a-spacing-small']

*** Keywords ***
Verify page loaded
    Page Should Contain Element             ${SIGNIN_MAIN_HEADING}
    Element Text Should Be                  ${SIGNIN_MAIN_HEADING}    Sign in