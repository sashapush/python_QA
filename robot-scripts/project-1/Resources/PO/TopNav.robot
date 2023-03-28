*** Settings ***
Library    SeleniumLibrary
*** Variables ***
${TOPNAV_SEARCH_BAR} =       id=twotabsearchtextbox
${TOPNAV_SEARCH_BUTTON} =    xpath=//*[@id="nav-search-submit-button"]

*** Keywords ***
Search For Products
    Enter Search Term
    Submit Search

Enter Search Term
    Input Text                              ${TOPNAV_SEARCH_BAR}    ${SEARCH_TERM}
Submit Search
    Click Button                            ${TOPNAV_SEARCH_BUTTON}