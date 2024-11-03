*** Settings ***
Library    SeleniumLibrary
Resource    C:/Users/Shree/Desktop/New_Python/Data_driven_testing/drivenone.robot
Suite Setup    Open my browser
Suite Teardown    close browsers
Test Template    Invalid Login

*** Test Cases ***      username        password
Right user empty pass   admin          ${EMPTY}
Right user wrong pass   admin123        admin123
Wrong user right pass   Admin1           admin123
Wrong user empty pass   Admin        admin123
#All Right crediceladl   Admin           admin123


*** Keywords ***
Invalid Login
    [Arguments]    ${username}      ${password}
    Input username    ${username}
    Input Pwd    ${password}
    click login button
    Error message visible as


