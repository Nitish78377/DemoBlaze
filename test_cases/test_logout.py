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
    def test_logout(self, setup):
        self.driver = setup
        self.driver.get(BasePage.Page_url)
        time.sleep(2)
        self.lp = Login_Page(self.driver)
        self.lp.click_login()
        time.sleep(2)
        self.lp.enter_username(BasePage.Valid_User_Name)
        self.lp.enter_password(BasePage.Valid_Password)
        self.lp.click_user_loginbtn()
        time.sleep(3)
        self.lp.click_on_logout_btn()
        time.sleep(3)
        self.hp = Home_Page(self.driver)
        homepage_text = self.hp.homepage_text()
        print(homepage_text)
        if homepage_text == TestData.HOMEPAGE_TEXT:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("..\\ScreenShots\\test_logout.png")
            self.driver.close()
            assert False
