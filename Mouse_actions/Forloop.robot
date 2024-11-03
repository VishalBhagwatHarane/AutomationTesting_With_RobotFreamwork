*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
ForLoop1
    [Tags]  sanity
    FOR    ${i}    IN RANGE    0    10
       Log To Console    ${i}
    END


ForLoop2
    [Tags]    regression
    FOR    ${ii}    IN    1    2    3    4    5    6    7    8
        Log To Console    ${ii}
    END

ForLoop3
    @{item}     create list    1   2   3   4   5
    FOR    ${i}     IN  @{item}
        LOG TO CONSOLE  ${i}
    END

ForLoop4
    [Tags]    regression
    FOR    ${i}     IN      Vishal  Mayur   Rishikesh   Krishna     Shilok
    log to console    ${i}
    END

ForLoop5
    [Tags]    sanity
    @{namelist}     create list    Arti vishal harane bhagwat Rukhminna
    FOR    ${i}     IN    @{namelist}
    log to console    @{namelist}
    END

ForLoop6Exit
    @{item}     create list    1    2   3   4   5
    FOR     ${i}    IN    @{item}
        log to console    ${i}
        exit for loop if   ${i} == 3
    END


