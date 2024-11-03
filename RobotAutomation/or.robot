*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://opensource-demo.orangehrmlive.com/web/index.php/auth/login


*** Test Cases ***
LoginTest
    open Browser    ${url}   ${browser}
    loginApplication
    capture Page Screenshot
    close Browser

*** Keywords ***
loginApplication
    sleep    9
    input Text    xpath://input[@placeholder='Username']    Admin
    sleep    4
    input Text    xpath://input[@placeholder='Password']    admin123
    sleep    3
    click Button    xpath://button[@type='submit']
    sleep    6
