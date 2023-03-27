# robot -d results .\Tests\passing.robot
*** Settings ***
Library    SeleniumLibrary
*** Variables ***

*** Test Cases ***
User can search for products
    @{url_and_browser} =    Set Variable    https://www.amazon.com    chrome
    #Begin Web Test    https://www.amazon.com    firefox
    Begin Web Test    ${url_and_browser}
*** Keywords ***
#Begin Web Test
#    [Arguments]    ${url}    ${browser}
#    Open Browser     ${url}    ${browser}
#    Close Browser

Begin Web Test
    [Arguments]    ${url_and_browser}
    Open Browser     ${url_and_browser}[0]    ${url_and_browser}[1]
    Close Browser