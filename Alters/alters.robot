*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
AltersTestCases
    open browser    https://testautomationpractice.blogspot.com/    chrome
    click button    xpath://button[@onclick='myFunctionAlert()']
    sleep    5
#    handle alert    accept
#    handle alert    dismiss
#    alert should be present    I am an alert box!
#    alert should not be present    I am an alert box!
    sleep    5