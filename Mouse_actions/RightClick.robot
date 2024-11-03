*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Mouse_Click
    #right click buton open context menu
    open browser    https://swisnl.github.io/jQuery-contextMenu/demo.html   chrome
    maximize browser window
    open context menu    xpath://section[@class='wy-nav-content-wrap']//ul[1]//li[1]//following::span[@class='context-menu-one btn btn-neutral']
    sleep    5

    #Dupluec click action
    go to    https://testautomationpractice.blogspot.com/
    scroll element into view    xpath://p[normalize-space()='Drag me to my target']
    double click element    xpath://button[normalize-space()='Copy Text']
    sleep   3
    #drag and drop action
    go to    http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html
    maximize browser window
    drag and drop    id:box3    id:box103

