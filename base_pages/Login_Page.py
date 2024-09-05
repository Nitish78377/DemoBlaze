import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By


class Login_Page:
    """Page Objects"""
    logout_btn_xpath = "//a[text()='Log out']"
    login_welcome_text_xpath = "//a[text()='Welcome Nitish']"
    textbox_username_id = 'loginusername'
    textbox_password_id = 'loginpassword'
    btn_login_xpath = "//a[text()='Log in']"
    user_login_xpath = "//button[text()='Log in']"
    btn_logout_xpath = "//a[text()='Log out']"
    login_page_title_xpath = "//h5[text()='Log in']"
    login_page_closebtn_xpath = "//div[@id='logInModal']//button[text()='Close']"
    login_page_username_field_xpath = "//div[@class='form-group']//label[text()='Username:' and @for='log-name']"
    login_page_password_field_xpath = "//div[@class='form-group']//label[text()='Password:' and @for='log-pass']"
    login_page_crossbtn_xpath = "//div[@id='logInModal']//button[@class='close']"

    def __init__(self, driver):
        self.driver = driver

        """Page Actions"""

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

    def click_user_loginbtn(self):
        self.driver.find_element(By.XPATH, self.user_login_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.btn_logout_xpath).click()

    def login_page_title_text(self):
        title = self.driver.find_element(By.XPATH, self.login_page_title_xpath).text
        return title

    def click_login_closebtn(self):
        self.driver.find_element(By.XPATH, self.login_page_closebtn_xpath).click()

    def click_login_crossbtn(self):
        self.driver.find_element(By.XPATH, self.login_page_crossbtn_xpath).click()

    def login_page_userField_text(self):
        text = self.driver.find_element(By.XPATH, self.login_page_username_field_xpath).text
        return text

    def login_page_passwordField_text(self):
        text = self.driver.find_element(By.XPATH, self.login_page_password_field_xpath).text
        return text

    def login_valid_user_welcome_text(self):
        welcome_text=self.driver.find_element(By.XPATH,self.login_welcome_text_xpath).text
        return welcome_text

    def click_on_logout_btn(self):
        self.driver.find_element(By.XPATH,self.logout_btn_xpath).click()
