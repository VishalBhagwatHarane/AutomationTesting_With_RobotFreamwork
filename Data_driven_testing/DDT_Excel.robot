*** Settings ***
Library    SeleniumLibrary
#Library    ExcelLibrary
Resource    C:/Users/Shree/Desktop/New_Python/Data_driven_testing/drivenone.robot
Library     DataDriver  C:/Users/Shree/Desktop/New_Python/TestData.xlsx  sheet_name=Sheet1
Suite Setup    Open my browser
Suite Teardown    close browsers
Test Template   Invalid Login
Library    SeleniumLibrary
Resource    C:/Users/Shree/Desktop/New_Python/Data_driven_testing/drivenone.robot
Library    DataDriver  ../New_Python/TestData.xlsx  sheet_name=Sheet1
*** Test Cases ***
LoginTestWithExcel using ${username}  and   ${password}


*** Keywords ***
Invalid Login
    [Arguments]    ${username}    ${password}
    Input username   ${username}
    Input Pwd    ${password}
    click login button
    Error message visible as
