*** Settings ***
Library      SeleniumLibrary

*** Variables ***
${Browser}  headlesschrome
${Url}  https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407

*** Test Cases ***
Form Filling
    Open Browser     ${Url}     ${Browser}
    maximize browser window
    Sleep    5

    # Fill text fields
    Input Text    //input[@id='RESULT_TextField-1']    Vishal
    Input Text    //input[@id='RESULT_TextField-2']    Harane
    Input Text    //input[@name='RESULT_TextField-3']   992155454

    Sleep    2

    # Scroll to the checkbox and select the radio button
    Scroll Element Into View    //label[@for='RESULT_CheckBox-8_0']
    Sleep    2
    Select Radio Button    //input[@id='RESULT_RadioButton-7_0']   Radio-1

    Sleep    2
    Close Browser

