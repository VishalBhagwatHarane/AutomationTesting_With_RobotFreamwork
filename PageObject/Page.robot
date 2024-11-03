*** Settings ***
Library    SeleniumLibrary
Variables    C:/Users/Shree/Desktop/New_Python/PageObject/Locatores.py

*** Keywords ***
Open my Browser
    [Arguments]    ${SiteUrl}   ${Brwoser}
    open browser   ${SiteUrl}   ${Brwoser}
    close browser
Enter UserName
    [Arguments]    ${username}
    input text    ${txt_UserName}   ${username}
Enter Password
    [Arguments]    ${PASSWORDS}
    input text    ${txt_Password}     ${PASSWORDS}
click Login
    click button    ${click_button}
Verfiy Successfull Login
    title should be    OrangeHRM
close My browser
    CLOSE ALL BROWSERS

