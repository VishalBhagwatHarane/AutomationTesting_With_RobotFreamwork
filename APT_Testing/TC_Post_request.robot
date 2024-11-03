*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Variables ***
${base_url}=    https://simple-books-api.glitch.me

*** Test Cases ***
Post_Information_Request
    create session    mysession     ${base_url}

    # Creating a dictionary to use as the request body
    ${body}=    create dictionary   id=21   name=Washington Maharastra   type=fiction   available=true

    # Sending a POST request to the /register endpoint
    ${response}=    post request    mysession     /register   json=${body}
    log to console    ${response.status_code}
    log to console    ${response.content}
