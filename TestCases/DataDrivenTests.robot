*** Settings ***
Documentation   Sample Data Driven Testing Exercise
Library         SeleniumLibrary
Library         DataDriver      file=TestData/submitFeedback.csv
Library         ../Pages/BasePage.py
Library         ../Pages/HomePage.py
Library         ../Pages/ContactPage.py
Test Template   Verify Feedback Is Successfully Submitted

*** Variables ***

*** Keywords ***
Verify Feedback Is Successfully Submitted
    [Arguments]     ${forename}     ${email}    ${message}
    Open Browser To Jupiter Toys Home Page
    Navigate To Contact
    Populate Mandatory Fields   ${forename}     ${email}    ${message}
    Submit Feedback
    Verify Feedback Successful Submission Message   ${forename}
    Close Browser

*** Test Cases ***
Verify User Is Able To Submit Feedback