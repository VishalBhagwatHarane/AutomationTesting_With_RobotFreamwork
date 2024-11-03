*** Settings ***
Library    SeleniumLibrary
Resource    C:/Users/Shree/Desktop/New_Python/User_Defined_Keywords/resources.robot

*** Variables ***
${URL}  https://demo.guru99.com/test/newtours/
${Browser}  chrome

*** Test Cases ***
TC1
    ${Pagetitle}=    lanchBrowser    ${URL}  ${Browser}
    log to console   ${Pagetitle}
    log    ${Pagetitle}
    input text    name:userName    mercury
    input text    name:password    mercury
    click button    name:submit
    sleep    3
#    ${title1}=   get title
#    [Return]    ${title1}
