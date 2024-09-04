import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.Login_Page import Login_Page
from utilities.read_properties import Read_Config
from Test_Data.TestData import TestData
from Configurations.basefile import BasePage
from base_pages.Home_Page import Home_Page
from base_pages.SignUp_Page import SignUp_Page


class Test_SignUp_Page:
    @pytest.mark.sanity
    def test_signup_page_title(self, setup):
        self.driver = setup
        self.driver.get(BasePage.Page_url)
        time.sleep(2)
        self.sp = SignUp_Page(self.driver)
        self.sp.click_on_signup_page()
        time.sleep(5)
        signup_title = self.sp.signup_page_title_text()
        exp_title = TestData.SignUp_Page_title
        if signup_title == exp_title:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("..\\ScreenShots\\test_signup_page_title.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    def test_valid_signup(self, setup):
        self.driver = setup
        self.driver.get(BasePage.Page_url)
        time.sleep(2)
        self.sp = SignUp_Page(self.driver)
        self.sp.click_on_signup_page()
        time.sleep(3)
        self.sp.enter_username(TestData.Signup_page_username)
        self.sp.enter_password(TestData.Signup_page_password)
        time.sleep(5)
        self.sp.click_on_signup_btn()
        time.sleep(2)
        alert = self.driver.switch_to
        success_message = alert.alert.text
        if success_message == TestData.Signup_successful_message:
            assert True
            alert.alert.accept()
            self.driver.close()
        else:
            self.driver.save_screenshot("..\\ScreenShots\\test_valid_signup.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    def test_invalid_signup(self, setup):
        self.driver = setup
        self.driver.get(BasePage.Page_url)
        time.sleep(2)
        self.sp = SignUp_Page(self.driver)
        self.sp.click_on_signup_page()
        time.sleep(3)
        self.sp.enter_username(TestData.Signup_page_username_invalid)
        self.sp.enter_password(TestData.Signup_page_password)
        time.sleep(5)
        self.sp.click_on_signup_btn()
        time.sleep(2)
        alert = self.driver.switch_to
        success_message = alert.alert.text
        if success_message == TestData.Signup_successful_message:
            alert.alert.accept()
            self.driver.close()
            self.driver.save_screenshot("..\\ScreenShots\\test_valid_signup.png")
            assert False
        else:
            assert True
            self.driver.close()

    @pytest.mark.sanity
    def test_signup_only_with_username(self, setup):
        self.driver = setup
        self.driver.get(BasePage.Page_url)
        time.sleep(2)
        self.sp = SignUp_Page(self.driver)
        self.sp.click_on_signup_page()
        time.sleep(3)
        self.sp.enter_username(TestData.Signup_page_username)
        time.sleep(3)
        self.sp.click_on_signup_btn()
        time.sleep(2)
        alert = self.driver.switch_to
        error_message = alert.alert.text
        if error_message == TestData.invalid_username_and_password_text:
            assert True
            alert.alert.accept()
            self.driver.close()
        else:
            self.driver.save_screenshot("..\\ScreenShots\\test_signup_only_with_username.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    def test_signup_with_only_password(self, setup):
        self.driver = setup
        self.driver.get(BasePage.Page_url)
        time.sleep(2)
        self.sp = SignUp_Page(self.driver)
        self.sp.click_on_signup_page()
        time.sleep(3)
        self.sp.enter_password(TestData.Signup_page_password)
        time.sleep(2)
        self.sp.click_on_signup_btn()
        time.sleep(2)
        alert = self.driver.switch_to
        error_message = alert.alert.text
        if error_message == TestData.invalid_username_and_password_text:
            assert True
            alert.alert.accept()
            self.driver.close()
        else:
            self.driver.save_screenshot("..\\ScreenShots\\test_signup_with_only_password.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    def test_signup_page_closebtn(self, setup):
        self.driver = setup
        self.driver.get(BasePage.Page_url)
        time.sleep(2)
        self.sp = SignUp_Page(self.driver)
        self.sp.click_on_signup_page()
        self.sp.click_on_close_btn()
        time.sleep(3)
        self.hp = Home_Page(self.driver)
        homepage_text = self.hp.homepage_text()
        if homepage_text == TestData.HOMEPAGE_TEXT:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("..\\ScreenShots\\test_login_page_closebtn.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    def test_all_signup_fields(self, setup):
        self.driver = setup
        self.driver.get(BasePage.Page_url)
        time.sleep(2)
        self.sp = SignUp_Page(self.driver)
        self.sp.click_on_signup_page()
        time.sleep(2)
        userNameField_text = self.sp.signup_page_userField_text()
        passwordField_text = self.sp.signup_page_passwordField_text()
        if userNameField_text == TestData.UserName_field_text and passwordField_text == TestData.Password_field_text:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("..\\ScreenShots\\test_all_signup_fields.png")
            self.driver.close()
            assert False


