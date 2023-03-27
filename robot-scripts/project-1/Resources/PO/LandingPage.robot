*** Settings ***
Library  SeleniumLibrary

*** Variables ***

*** Keywords ***
Load
    Go to    ${START_URL}

Verify page loaded
    Wait Until Page Contains                Search Amazon