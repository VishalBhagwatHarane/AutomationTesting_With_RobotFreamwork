*** Settings ***
Library    SeleniumLibrary
Resource    C:/Users/Shree/Desktop/New_Python/PageObject/Page.robot

*** Variables ***
${Brwoser}  headlesschrome
${SiteUrl}  https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${user}     Admin
${Password}  admin123

*** Test Cases ***
LoginTest
    Open my Browser  ${SiteUrl}    ${Brwoser}
    sleep    3
    Enter UserName    ${user}
    sleep    3
    Enter Password    ${Password}
    click Login