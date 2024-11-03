*** Settings ***
Library    SeleniumLibrary



*** Keywords ***
lanchBrowser
    [Arguments]    ${appurl}    ${appBrowser}
    open browser   ${appurl}    ${appBrowser}
    maximize browser window
    sleep    3
    ${title}=   get title
    [Return]    ${title}