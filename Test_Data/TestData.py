import math
import random


class TestData:
    HOMEPAGE_TITLE = "STORE"
    HOMEPAGE_TEXT = "PRODUCT STORE"

    # Login Page

    LOGIN_PAGE_TITLE = "Log in"

    #     error messages
    Wrong_password_alert_text = "Wrong password."
    Wrong_username_password_alert_text = "Please fill out Username and Password."

#     LoginPage

    UserName_field_text = "Username:"
    Password_field_text = "Password:"

#     cart Page
    Cart_page_title_text = "Products"

#     Product Page

    Product_text = "Nokia lumia 1520"
    Laptops_category_product_text = "Sony vaio i5"
    Monitors_category_product_text = "Apple monitor 24"
    NextBtn_Product_text  = 'MacBook air'

# Product description page

    product_description_page_text = "Product description"
    Add_to_cart_text = "Product added."

#     place order
    Name = "Test-0"
    Country = "Test-1"
    City = "Test-2"
    Credit_Card = "123456789"
    Month = "Sept"
    Year = "2024"
    Purchase_Successfull_text = "Thank you for your purchase!"

#     SignUp page
    random_values = random.randint(1,10000)
    String = str(random_values)
    SignUp_Page_title = "Sign up"
    Signup_page_username = "Test"+String
    Signup_page_username_invalid = random_values
    Signup_page_password = "123456"
    Signup_successful_message = "Sign up successful."
    invalid_username_and_password_text = "Please fill out Username and Password."
