import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.Login_Page import Login_Page
from utilities.read_properties import Read_Config
from Test_Data.TestData import TestData
from Configurations.basefile import BasePage
from base_pages.Home_Page import Home_Page


class Test_Login_Page:

    @pytest.mark.sanity
    def test_loginPage_title(self,setup):
        self.driver = setup
        self.driver.get(BasePage.Page_url)
        time.sleep(2)
        self.lp = Login_Page(self.driver)
        self.lp.click_login()
        time.sleep(3)
        login_title = self.lp.login_page_title_text()
        exp_title = TestData.LOGIN_PAGE_TITLE
        if login_title == exp_title:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("..\\ScreenShots\\test_login_page_title.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    def test_valid_login(self,setup):
        self.driver = setup
        self.driver.get(BasePage.Page_url)
        time.sleep(2)
        self.lp = Login_Page(self.driver)
        self.lp.click_login()
        time.sleep(2)
        self.lp.enter_username(BasePage.Valid_User_Name)
        self.lp.enter_password(BasePage.Valid_Password)
        self.lp.click_user_loginbtn()
        time.sleep(5)
        login_txt = self.lp.login_valid_user_welcome_text()
        if login_txt == BasePage.login_verification:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("..\\ScreenShots\\test_valid_login.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    def test_invalid_login(self,setup):
        self.driver = setup
        self.driver.get(BasePage.Page_url)
        time.sleep(2)
        self.lp = Login_Page(self.driver)
        self.lp.click_login()
        time.sleep(2)
        self.lp.enter_username(BasePage.Invalid_User_Name)
        self.lp.enter_password(BasePage.Invalid_Password)
        self.lp.click_user_loginbtn()
        time.sleep(5)
        alert = self.driver.switch_to
        error_msg = alert.alert.text
        if error_msg == TestData.Wrong_password_alert_text:
            assert True
            self.driver.quit()
        else:
            self.driver.save_screenshot("..\\ScreenShots\\test_invalid_login.png")
            self.driver.quit()
            assert False

    @pytest.mark.sanity
    def test_login_with_only_username(self,setup):
        self.driver = setup
        self.driver.get(BasePage.Page_url)
        time.sleep(2)
        self.lp = Login_Page(self.driver)
        self.lp.click_login()
        time.sleep(2)
        self.lp.enter_username(BasePage.Valid_User_Name)
        self.lp.click_user_loginbtn()
        time.sleep(5)
        alert = self.driver.switch_to
        error_msg = alert.alert.text
        if error_msg == TestData.Wrong_username_password_alert_text:
            assert True
            self.driver.quit()
        else:
            self.driver.save_screenshot("..\\ScreenShots\\test_login_with_only_username.png")
            self.driver.quit()
            assert False

    @pytest.mark.sanity
    def test_login_with_only_password(self,setup):
        self.driver = setup
        self.driver.get(BasePage.Page_url)
        time.sleep(2)
        self.lp = Login_Page(self.driver)
        self.lp.click_login()
        time.sleep(2)
        self.lp.enter_password(BasePage.Valid_Password)
        self.lp.click_user_loginbtn()
        time.sleep(5)
        alert = self.driver.switch_to
        error_msg = alert.alert.text
        if error_msg == TestData.Wrong_username_password_alert_text:
            assert True
            self.driver.quit()
        else:
            self.driver.save_screenshot("..\\ScreenShots\\test_login_with_only_password.png")
            self.driver.quit()
            assert False

    @pytest.mark.sanity
    def test_login_page_closebtn(self,setup):
        self.driver = setup
        self.driver.get(BasePage.Page_url)
        time.sleep(2)
        self.lp = Login_Page(self.driver)
        self.lp.click_login()
        self.hp = Home_Page(self.driver)
        time.sleep(2)
        self.lp.click_login_closebtn()
        homepage_text = self.hp.homepage_text()
        if homepage_text == TestData.HOMEPAGE_TEXT:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("..\\ScreenShots\\test_login_page_closebtn.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    def test_all_loginPage_fields(self,setup):
        self.driver = setup
        self.driver.get(BasePage.Page_url)
        time.sleep(2)
        self.lp = Login_Page(self.driver)
        self.lp.click_login()
        time.sleep(2)
        userNameField_text = self.lp.login_page_userField_text()
        passwordField_text = self.lp.login_page_passwordField_text()
        if userNameField_text == TestData.UserName_field_text and passwordField_text == TestData.Password_field_text:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("..\\ScreenShots\\test_all_loginPage_fields.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    def test_loginPage_crossbtn(self,setup):
        self.driver = setup
        self.driver.get(BasePage.Page_url)
        time.sleep(2)
        self.lp = Login_Page(self.driver)
        self.lp.click_login()
        self.hp = Home_Page(self.driver)
        time.sleep(2)
        self.lp.click_login_crossbtn()
        homepage_text = self.hp.homepage_text()
        if homepage_text == TestData.HOMEPAGE_TEXT:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("..\\ScreenShots\\test_loginPage_crossbtn.png")
            self.driver.close()
            assert False








