*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URl}  https://demo.automationtesting.in/Windows.html
${Browser}  chrome
${Button_alter}  xpath=//a[normalize-space()='Alert with OK & Cancel']
${button_uu}    xpath=//button[@class='btn btn-primary']
*** Test Cases ***
Mytestcases
    open browser  ${URl}   ${Browser}
    sleep    5
    alterss
#    sleep    2
#    click button    xpath=//button[@class='btn btn-info']
#    sleep    2
#    input text into alert    Vishal
#    sleep    2

    close browser
*** Keywords ***
alterss
    click button    ${Button_alter}}
    sleep    5
    click button    ${button_uu}
    handle alert    accept
