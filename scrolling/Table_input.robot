*** Settings ***
Library    SeleniumLibrary

*** Variables ***

*** Test Cases ***
Table1
    open browser    https://testautomationpractice.blogspot.com/    chrome
    maximize browser window
    scroll element into view    xpath://th[normalize-space()='Name']
#    xpath://table[@name="BookTable"]/tbody/tr/td[1]    ## table xpath
#    //table[@name="BookTable"]/tbody/tr[1]/th ##heder expath
    ${rows}=   get element count    xpath://table[@name="BookTable"]/tbody/tr
    ${cols}=    get element count    xpath://table[@name="BookTable"]/tbody/tr[1]/th

    log to console       ${rows}
    log to console       ${cols}

    ${data}=    get element count    xpath://table[@name="BookTable"]/tbody/tr[5]/td[1]
    log to console    ${data}
    sleep    6
    table column should contain    xpath://table[@name="BookTable"]    2    Author
    table row should contain    xpath://table[@name="BookTable"]    4   Learn JS
    table cell should contain   xpath://table[@name="BookTable"]    5   2   Mukesh
#    table header should contain  xpath://table[@name="BookTable"]    BookTable