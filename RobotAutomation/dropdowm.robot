*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${username}    Admin
${password}    admin123

*** Test Cases ***
TestingInputBox
    Open Browser    ${url}  ${browser}
    Maximize Browser Window
    LoginTest
    Close Browser

*** Keywords ***
LoginTest
    sleep    5
    title should be   OrangeHRM    10s
    ${Username_input}    Set Variable    xpath://input[@placeholder='Username']
    ${Password_input}    Set Variable    xpath://input[@placeholder='Password']

    Element Should Be Visible    ${Username_input}
    Element Should Be Enabled    ${Username_input}
    Element Should Be Visible    ${Password_input}
    Element Should Be Enabled    ${Password_input}

    Input Text    ${Username_input}    ${username}
    Input Text    ${Password_input}    ${password}

    Click Button    xpath://button[@type='submit']
    sleep    10
    Click link      //a[normalize-space()='My Info']
    sleep    10
    scroll element into view    //body/div[@id='app']/div[@class='oxd-layout orangehrm-upgrade-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[1]
    sleep    10
    select radio button    Gender   1
    # Correct locator for selecting "Male" radio button
#    select radio button     xpath://label[normalize-space()='Female']
#    sleep    5
