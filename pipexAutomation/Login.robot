*** Settings ***
Library    SeleniumLibrary

*** Variables ***


*** Test Cases ***
PipexAutomation
    open browser    https://www.saucedemo.com/  chrome
    maximize browser window
    sleep    4
    input text    xpath://input[@id='user-name']  standard_user
    sleep    6
    input text    xpath://input[@id='password']     secret_sauce
    sleep    4
    click button    //input[@id='login-button']
    sleep    5
    click button    xpath://button[@id='add-to-cart-sauce-labs-backpack']
    sleep    3



*** Keywords ***
