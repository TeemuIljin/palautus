*** Settings ***
Resource    ${CURDIR}/resource.robot
Test Setup  Create User And Input Login Command

*** Test Cases ***
Login With Incorrect Password
    Input Credentials    kalle    wrongpassword
    Run Application
    Application Output Should Contain    Invalid username or password

Login With Nonexistent Username
    Input Credentials    doesnotexist    somepass123
    Run Application
    Application Output Should Contain    Invalid username or password
