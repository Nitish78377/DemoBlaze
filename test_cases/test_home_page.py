import time
import pytest
from Test_Data.TestData import TestData
from Configurations.basefile import BasePage
from selenium.webdriver.common.by import By
from base_pages.Home_Page import Home_Page


class Test_Home_Page:
    @pytest.mark.sanity
    def test_homepage_title_verification(self, setup):
        self.driver = setup
        self.driver.get(BasePage.Page_url)
        time.sleep(2)
        act_title = self.driver.title
        exp_title = TestData.HOMEPAGE_TITLE
        if act_title == exp_title:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\ScreenShots\\test_title_verification.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    def test_homepage_visible(self, setup):
        self.driver = setup
        self.driver.get(BasePage.Page_url)
        time.sleep(2)
        self.hp = Home_Page(self.driver)
        homepage_text = self.hp.homepage_text()
        print(homepage_text)
        if homepage_text == TestData.HOMEPAGE_TEXT:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("..\\ScreenShots\\test_homepage_visible.png")
            self.driver.close()
            assert False
