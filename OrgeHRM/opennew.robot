*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
My TestCase
    open browser    https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407  headlesschrome
    maximize browser window
    open browser    https://www.saucedemo.com/    chrome

    close all browsers
