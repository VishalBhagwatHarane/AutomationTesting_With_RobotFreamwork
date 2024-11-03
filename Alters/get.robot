*** Settings ***
Library    RequestsLibrary

*** Variables ***
${base_url}    https://simple-books-api.glitch.me
${books_endpoint}    /books

*** Test Cases ***
Get_Books_Info
    # Create a session with the base URL
    Create Session    mysession    ${base_url}

    # Perform a GET request to the books endpoint
    ${response}=    Get Request    mysession    ${books_endpoint}

    # Log the status code
    Log To Console    Status Code: ${response.status_code}

    # Log the response content
    Log To Console    Response Content: ${response.content}

    # Log the headers of the response
    Log To Console    Response Headers: ${response.headers}

    # Assert the response status code is 200 (OK)
    Should Be Equal As Numbers    ${response.status_code}    200
