*** Settings ***
Library    SeleniumLibrary



*** Variables ***



*** Test Cases ***
LoginTest
    open browser    https://demo.nopcommerce.com/login?returnUrl=%2F    chrome
    click link    xpath://a[@class='ico-login']
    input text    id:Email  pavanoltraning@gmail.com
    input text    id:Password   Test@123
    click element    xpath://button[normalize-space()='Log in']
    close browser


*** Keywords ***
