*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
ScrollingTesting
    open browser    https://www.tableau.com/    chrome
    maximize browser window
#    execute javascript    window.scrollTo(0,1500)
#    sleep    3
#    scroll element into view    xpath://section[@id='paragraph-id--219133']
    execute javascript    window.scrollTo(0,document.body.scrollHeight)
    sleep    3
    execute javascript    window.scrollTo(0,-document.body.scrollHeight)
    sleep    3