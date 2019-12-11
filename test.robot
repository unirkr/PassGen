*** Settings ***
Documentation   This is basic information
Library   SeleniumLibrary

*** Test Cases ***
User sign-in
    [Documentation]     User Sign in
    ## to run -> robot -d results tests/test.robot
    Open Browser    http://www.amazon.com   chrome
    Sleep  2s
    Close Browser
