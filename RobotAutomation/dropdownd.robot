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
    SelectGenderFemale
    Close Browser

*** Keywords ***
LoginTest
    sleep    5
    Title Should Be   OrangeHRM    10s
    ${Username_input}    Set Variable    xpath://input[@placeholder='Username']
    ${Password_input}    Set Variable    xpath://input[@placeholder='Password']

    Element Should Be Visible    ${Username_input}
    Element Should Be Enabled    ${Username_input}
    Element Should Be Visible    ${Password_input}
    Element Should Be Enabled    ${Password_input}

    Input Text    ${Username_input}    ${username}
    Input Text    ${Password_input}    ${password}

    Click Button    xpath://button[@type='submit']
    sleep    5
    Click Link      xpath=//a[normalize-space()='My Info']
    sleep    5

SelectGenderFemale
    Scroll Element Into View    xpath=//label[normalize-space()='Gender']
    sleep    2
    Click Element   xpath=//input[@name='gender' and @value='2']
    sleep    5
