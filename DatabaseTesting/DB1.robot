*** Settings ***
Library    DatabaseLibrary
#Library    OperatingSystem

*** Variables ***
${DB_TYPE}      cx_Oracle
${DB_HOST}      localhost
${DB_PORT}      1521
${DB_SID}       xe
${DB_USER}      HR
${DB_PASSWORD}      HR

*** Test Cases ***
Connect And Query Oracle Database
    # Connect to Oracle database using cx_Oracle module
    Connect To Database    ${DB_TYPE}    ${DB_USER}    ${DB_PASSWORD}    ${DB_HOST}:${DB_PORT}/${DB_SID}
    ${query_result}    check if exists in database    SELECT * FROM employees WHERE department_id = 90
    Log    ${query_result}
    Disconnect From Database