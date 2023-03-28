*** Settings ***
Library  SeleniumLibrary
*** Variables ***
${SIGNIN_MAIN_HEADING} =    css=h1[class='a-spacing-small']

*** Keywords ***
Verify page loaded
    Page Should Contain Element             ${SIGNIN_MAIN_HEADING}
    Element Text Should Be                  ${SIGNIN_MAIN_HEADING}    Sign in

Login With Valid Credentials
    [Arguments]    ${Username}    ${Password}
    Fill "Email" Field    ${Username}
    Fill "Password" Field    ${Password}
    Click "Submit" Button

Fill "Email" Field
    [Arguments]     ${Username}
    Log    Filling email field with ${Username}

Fill "Password" Field
    [Arguments]     ${Password}
    Log    Filling password field with ${Password}

Click "Submit" Button
    Log    Clicking submit button