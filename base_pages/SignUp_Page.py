import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By


class SignUp_Page:
    """Page Objects"""

    signup_page_nav_xpath = "//a[@id='signin2' and text()='Sign up']"
    signup_page_title_xpath = "//h5[text()='Sign up']"
    signup_page_username_ID = 'sign-username'
    signup_page_password_ID = 'sign-password'
    signup_btn_xpath = "//button[text()='Sign up']"
    signup_page_close_btn = "//div[@id='signInModal']//button[text()='Close']"
    signup_page_username_text_xpath = "//label[text()='Username:' and @for='sign-username']"
    signup_page_password_text_xpath = "//label[text()='Password:' and @for='sign-password']"

    def __init__(self, driver):
        self.driver = driver

        """Page Actions"""

    def click_on_signup_page(self):
        self.driver.find_element(By.XPATH, self.signup_page_nav_xpath).click()

    def signup_page_title_text(self):
        title = self.driver.find_element(By.XPATH, self.signup_page_title_xpath).text
        return title

    def enter_username(self,username):
        self.driver.find_element(By.ID,self.signup_page_username_ID).clear()
        self.driver.find_element(By.ID,self.signup_page_username_ID).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(By.ID,self.signup_page_password_ID).clear()
        self.driver.find_element(By.ID,self.signup_page_password_ID).send_keys(password)

    def signup_page_userField_text(self):
        text = self.driver.find_element(By.XPATH, self.signup_page_username_text_xpath).text
        return text

    def signup_page_passwordField_text(self):
        text = self.driver.find_element(By.XPATH, self.signup_page_password_text_xpath).text
        return text

    def click_on_signup_btn(self):
        self.driver.find_element(By.XPATH,self.signup_btn_xpath).click()

    def click_on_close_btn(self):
        self.driver.find_element(By.XPATH,self.signup_page_close_btn).click()
