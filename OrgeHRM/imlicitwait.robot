*** Settings ***
Library    SeleniumLibrary

*** Variables ***


*** Test Cases ***
Form Filling
    open browser  https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407    headlesschrome
    maximize browser window
    set selenium implicit wait    10 seconds
    input text    RESULT_TextField-1    Vishal
    input text    RESULT_TextField-2    Harane
    input text    RESULT_TextField-3    9098898988
    input text    RESULT_TextField-4    india
    input text    RESULT_TextField-5    washim
    input text    RESULT_TextField-6    vishu@gmail.com
    scroll element into view    //label[@for='RESULT_CheckBox-8_4']
    click element    xpath=//label[@for='RESULT_RadioButton-7_0']
    click element    xpath=//label[@for='RESULT_CheckBox-8_0']
    click element    xpath=//label[@for='RESULT_CheckBox-8_1']
    click element    xpath=//label[@for='RESULT_CheckBox-8_2']
    click element    xpath=//label[@for='RESULT_CheckBox-8_3']
    click element    xpath=//label[@for='RESULT_CheckBox-8_4']
    click element    xpath=//label[@for='RESULT_CheckBox-8_5']
    click element    xpath=//label[@for='RESULT_CheckBox-8_6']
    select from list by label    RESULT_RadioButton-9   Afternoon
    select from list by index    RESULT_RadioButton-9   2

    Close Browser