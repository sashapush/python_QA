#robot -d results .\Tests\scalar_variables.robot
*** Settings ***
Resource    ../Resources/scope.robot

*** Variables ***
${MY_VARIABLE} =  Text and 12345
@{MY_LIST} =  1    2    3    4    5     #separate values by 2 spaces
${VAR} =  AppaData    #framework is case insensitive and will find this variable in lines 25 and 28; Set variables command not needed.
*** Test Cases ***
Variable demo
    Log    ${MY_VARIABLE}

Set a variable in test case
    ${tc_variable} =  Set Variable    My new variable
    Log    ${TC variable}

List Variable demo
    Log    ${MY_LIST}[0]
    Log    ${MY_LIST}[1]
    @{tc_var} =  Create List    First    Second
    Log    ${tc_var}[1]

Create variable
    #${var} =    Set Variable    AppaData
    Log    ${var}

Access variable
    Log    ${var}    #definition not found since var is TC scope only, line:24; once moved to variables - it works

*** Keywords ***
