*** Settings ***
Library  SeleniumLibrary
*** Variables ***
${FIRST_PRODUCT_PLACEHOLDER} =    xpath=//span[normalize-space()='Bburago B18-26017 1:24 Scale Race and Play of The Ferrari 458 Spider Sports Car Die-Cast Model']
${CLICKABLE_PRODUCT_LINK} =    css=div[class='s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_1'] a[class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']
*** Keywords ***
Verify Search Completed
    Wait Until Page Contains            results for "${SEARCH_TERM}"

Click Product Link
    [Documentation]  Something blabla
    Wait Until Element Is Visible           ${FIRST_PRODUCT_PLACEHOLDER}
    Click Link                              ${CLICKABLE_PRODUCT_LINK}
