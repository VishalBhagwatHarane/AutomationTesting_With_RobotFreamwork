*** Settings ***
Library  SeleniumLibrary


*** Test Cases ***
CountExtract1
    open browser    https://demo.guru99.com/test/newtours/      chrome
    maximize browser window
    ${Alllinkcount}=    get element count    xpath://a
    log to console   Total link count:${Alllinkcount}

    @{LinkItem}     create list
    FOR    ${i}    IN RANGE    1    ${Alllinkcount}+1
        @{linkItem}=     get text    xpath:xpath:(//a)[${i}]
        log to console    @{linkItem}
    END
    close browser

