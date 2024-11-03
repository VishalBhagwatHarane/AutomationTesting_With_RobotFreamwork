*** Settings ***
Library    SeleniumLibrary

*** Variables ***


*** Test Cases ***
RegisterTest
    open browser    https://demo.nopcommerce.com/register?returnUrl=%2F     chrome
    click button    xpath://input[@id='gender-male']
    input text      id:FirstName    Vish
    input text      id:LastName     Hara
    select from list by value    xpath://select[@name='DateOfBirthDay']     10
    select from list by value    xpath://select[@name='DateOfBirthMonth']       March
    select from list by value    xpath://select[@name='DateOfBirthYear']        2010


*** Keywords ***
