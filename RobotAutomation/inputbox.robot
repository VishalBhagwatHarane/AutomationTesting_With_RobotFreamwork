*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

*** Test Cases ***
TestingInputBox
    open browser    ${url}  ${browser}
    maximize browser window
    LoginoutTest
    close browser
*** Keywords ***
LoginoutTest
    sleep    5
    title should be    OrangeHRM
    sleep    6
    ${Username_txt}     set variable    xpath://input[@placeholder='Username']
    sleep    7
    ${Password_txt}     set variable    //input[@placeholder='Password']
    element should be visible    ${Username_txt}
    sleep    6
    element should be visible    ${Password_txt}
    sleep    6
    element should be enabled    ${Username_txt}
    sleep   5
    element should be enabled    ${Password_txt}

    input text    ${Username_txt}    Admin
    sleep    5
    input text    ${Password_txt}   admin123
    sleep    5
    click button    xpath://button[@type='submit']
    sleep    5
    click image    xpath://img[@class='oxd-userdropdown-img']
    sleep    3
    capture page screenshot
    sleep    5
    click link    xpath://a[normalize-space()='Logout']
    sleep    5
    capture page screenshot

