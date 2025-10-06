*** Settings ***
Documentation   Sample Exercise Using Selenium Library
Library         SeleniumLibrary
Library         ../Pages/BasePage.py
Library         ../Pages/HomePage.py
Library         ../Pages/ContactPage.py
Library         ../Pages/ShopPage.py
Library         ../Pages/CartPage.py

*** Variables ***

*** Keywords ***

*** Test Cases ***
Verify Contact Page Has Mandatory Input Fields
    Open Browser To Jupiter Toys Home Page
    Navigate To Contact
    Submit Feedback
    Verify Error Messages
    Populate Mandatory Fields   Tyrion  tyrion.lannister@got.com    Test from Tyrion    
    Verify No Error Messages Are Shown
    Close Browser

Verify Feedback Is Successfully Submitted
    Open Browser To Jupiter Toys Home Page
    Navigate To Contact
    Populate Mandatory Fields   Tyrion  tyrion.lannister@got.com    Test from Tyrion
    Submit Feedback
    Verify Feedback Successful Submission Message   Tyrion
    Close Browser

Verify The Total Price In The Cart
    Open Browser To Jupiter Toys Home Page
    Navigate To Shop
    Add Item To Cart    Stuffed Frog
    Add Item To Cart    Stuffed Frog
    Add Item To Cart    Fluffy Bunny
    Add Item To Cart    Valentine Bear
    Navigate To Cart
    Update Quantity Of Item    Fluffy Bunny    5
    Update Quantity Of Item    Valentine Bear  3
    Verify Price Of The Item     Stuffed Frog    $10.99
    Verify Price Of The Item     Fluffy Bunny    $9.99
    Verify Price Of The Item     Valentine Bear  $14.99
    Verify Subtotal Of The Item  Stuffed Frog    $21.98
    Verify Subtotal Of The Item  Fluffy Bunny    $49.95
    Verify Subtotal Of The Item  Valentine Bear  $44.97
    Verify The Total Price  Total: 116.9
    Close Browser