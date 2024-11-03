*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${browser}     headlesschrome
${Url}         https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${username}    Admin
${password}    admin123

*** Test Cases ***
Open_browser
    [Documentation]    Open browser, login, and navigate to 'My Info' section to select marital status.
    Open Browser    ${Url}  ${browser}
    Maximize Browser Window
    LoginTesting
    Close Browser

*** Keywords ***
LoginTesting
    Wait Until Element Is Visible    xpath://input[@placeholder='Username']    timeout=10s
    Input Text    xpath://input[@placeholder='Username']    ${username}
    Input Text    xpath://input[@placeholder='Password']    ${password}
    Click Button    xpath://button[@type='submit']
    Wait Until Element Is Visible    //a[normalize-space()='My Info']
    Click Link    //a[normalize-space()='My Info']
    Wait Until Element Is Visible    xpath://label[text()='Marital Status']/following::div[1]
    Click Element    xpath://label[text()='Marital Status']/following::div[1]  # Open dropdown
    Wait Until Element Is Visible    xpath://div[@role='option' and text()='Married']  # Replace 'Married' with the correct option text
    Click Element    xpath://div[@role='option' and text()='Married']
