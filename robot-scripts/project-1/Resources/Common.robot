*** Settings ***
Library    SeleniumLibrary
*** Keywords ***

Begin web test
    Open Browser                            about:blank       chrome
    Maximize Browser Window

End web test
    Close Browser