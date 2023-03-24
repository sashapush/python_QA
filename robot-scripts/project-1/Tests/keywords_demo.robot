*** Settings ***


*** Test Cases ***
Test case #1
    Do stuff    #it's user defined keyword
    Do other stuff

Test case #2
    Do something else
    Do other stuff

*** Keywords ***
Do stuff
    Log    I'm doing stuff right now!
Do other stuff
    Log    Doing other stuff!!!
Do something else
    Log    And finally i'm doing something else!!!@!#
