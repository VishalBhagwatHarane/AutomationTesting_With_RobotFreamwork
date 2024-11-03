*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${Login Url}    https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${browser}  chrome


*** Keywords ***
Open my browser
    open browser    ${Login Url}    ${browser}
    maximize browser window
    sleep    3
close browsers
    close all browsers
Input username
    [Arguments]    ${username}
    input text    //input[@placeholder='Username']   ${username}
    sleep    3
Input Pwd
    [Arguments]    ${password}
    input text    //input[@placeholder='Password']   ${password}
    sleep    3
click login button
    click button    //button[@type='submit']
    sleep    3
Error message visible as
    page should contain    Login was unsuccessfull

Dashboard page shoud be visible
    page should contain    Dashboard