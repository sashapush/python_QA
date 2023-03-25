*** Settings ***
Library  SeleniumLibrary

*** Variables ***

*** Keywords ***
Load
    Go to    http://www.amazon.com

Verify page loaded
    Wait Until Page Contains                Search Amazon