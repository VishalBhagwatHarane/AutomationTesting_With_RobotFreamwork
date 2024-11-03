*** Settings ***
Library    SeleniumLibrary



*** Variables ***



*** Test Cases ***
LoginTest
    open browser    https://opensource-demo.orangehrmlive.com/web/index.php/auth/login   chrome
    input text    xpath://input[@placeholder='Username']    Admin
    input text    xpath://input[@placeholder='Password']    admin123
    click button    xpath://button[@type='submit']
    sleep    4
    close browser


*** Keywords ***
