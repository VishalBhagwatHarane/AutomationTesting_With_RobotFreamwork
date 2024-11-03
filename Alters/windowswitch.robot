*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
MyTestCases
    open browser    https://demo.automationtesting.in/Windows.html  chrome
    click button    xpath://button[@class='btn btn-info'][normalize-space()='click']
    sleep    5
    switch window    title:Selenium
    sleep    5
    click element    xpath://a[normalize-space()='English']
    sleep    5
    click element    //a[normalize-space()='Other']
