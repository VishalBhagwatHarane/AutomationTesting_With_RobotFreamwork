*** Settings ***
Library    SeleniumLibrary


*** Variables ***
${browser}  headlesschrome
${Url}  https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${username}    Admin
${password}    admin123

*** Test Cases ***
Open_browser
    open browser    ${Url}  ${browser}
    maximize browser window
    LoginTesting
    close browser


*** Keywords ***
LoginTesting
    sleep    5
    # Checks that the page title is OrangeHRM
    title should be    OrangeHRM
    sleep    5
    input text    xpath://input[@placeholder='Username']        ${username}
    sleep    5
    input text    xpath://input[@placeholder='Password']        ${password}
    sleep    5
    click button    xpath://button[@type='submit']
    sleep    8
    click link    //a[normalize-space()='My Info']
#    sleep    5
#    select from list by label    xpath://i[@class='oxd-icon bi-caret-up-fill oxd-select-text--arrow']   Marital
    sleep    9
    select from list by index  xpath://i[@class='oxd-icon bi-caret-up-fill oxd-select-text--arrow']


