*** Settings ***
Resource    ${CURDIR}/resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Input New Command And Create User    newuser    GoodPass123
    Run Application
    Application Output Should Contain    User created

Register With Already Taken Username And Valid Password
    # First create the user, then attempt to create it again in the same run
    Input New Command And Create User    newuser    GoodPass123
    Input New Command And Create User    newuser    AnotherGood123
    Run Application
    Application Output Should Contain    Username already taken

Register With Too Short Username And Valid Password
    Input New Command And Create User    ab    GoodPass123
    Run Application
    Application Output Should Contain    Invalid username

Register With Enough Long But Invalid Username And Valid Password
    Input New Command And Create User    user_123    GoodPass123
    Run Application
    Application Output Should Contain    Invalid username

Register With Valid Username And Too Short Password
    Input New Command And Create User    freshuser    short
    Run Application
    Application Output Should Contain    Invalid password

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command And Create User    lettersonly    onlyletterslong
    Run Application
    Application Output Should Contain    Invalid password