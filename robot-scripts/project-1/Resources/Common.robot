*** Settings ***
Library    SeleniumLibrary
*** Variables ***


*** Keywords ***

Begin web test
    Open Browser                            about:blank       ${BROWSER}
    Maximize Browser Window

End web test
    Close Browser

Generate test data
    Log    I'm creating test data
    I'm another keyword    #we can use multiple keywords inside setup/teardown methods like this

Remove test data
    Log     I'm removing test data

I'm another keyword
    Log     Inside the keword