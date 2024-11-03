*** Settings ***
Library    SeleniumLibrary



*** Variables ***



*** Test Cases ***
LoginTest
    open browser    https://opensource-demo.orangehrmlive.com/web/index.php/auth/login   chrome
    sleep    6
    input text    xpath://input[@placeholder='Username']    Admin
    sleep    6
    input text    xpath://input[@placeholder='Password']    admin123
    sleep    6
#    click button    xpath://button[@type='submit']
    capture element screenshot  xpath://img[@alt='company-branding']    C:\Users\Shree\Desktop\New_Python\Alters\screeshot.png
    sleep    4
    close browser
