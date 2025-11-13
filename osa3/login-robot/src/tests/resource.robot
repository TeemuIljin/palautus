*** Settings ***
Library    ${CURDIR}/../AppLibrary.py

*** Keywords ***
Input Credentials
    [Arguments]    ${username}    ${password}
    Input    ${username}
    Input    ${password}
    # Do not run application here; let tests call Run Application once

Input New Command
    Input    new

Input New Command And Create User
    [Arguments]    ${username}    ${password}
    Input New Command
    Input    ${username}
    Input    ${password}
    # Do not run application here; let tests call Run Application once

Create User And Input Login Command
    [Arguments]    ${username}=kalle    ${password}=kalle123
    Input New Command And Create User    ${username}    ${password}
    Input    login