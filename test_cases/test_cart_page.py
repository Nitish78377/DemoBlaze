import time
import pytest
from Test_Data.TestData import TestData
from Configurations.basefile import BasePage
from selenium.webdriver.common.by import By
from base_pages.Home_Page import Home_Page
from base_pages.Login_Page import Login_Page
from base_pages.CheckOut_Page import CheckOut_Page
from base_pages.Product_Page import Product_Page
from base_pages.Cart_Page import  Cart_Page


class Test_Cart_Page:
    @pytest.mark.sanity
    def test_productAdded_to_cart(self, setup):
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
        self.pp = Product_Page(self.driver)
        self.pp.click_product()
        time.sleep(3)
        self.pp.click_addto_cartbtn()
        time.sleep(2)
        alert = self.driver.switch_to
        success_message = alert.alert.text
        if success_message == TestData.Add_to_cart_text:
            assert True
            alert.alert.accept()
            self.driver.close()
        else:
            self.driver.save_screenshot("..\\ScreenShots\\test_productAdded_to_cart.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    def test_cart_page_delete_btn(self, setup):
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
        self.pp = Product_Page(self.driver)
        self.pp.click_product()
        time.sleep(3)
        self.pp.click_addto_cartbtn()
        time.sleep(2)
        alert = self.driver.switch_to
        alert.alert.accept()
        self.cp = CheckOut_Page(self.driver)
        self.cp.click_cart_nav()
        time.sleep(3)
        self.cart_page = Cart_Page(self.driver)
        self.cart_page.click_on_delete_btn()
        act_title = self.cp.cart_page_title()
        exe_title = TestData.Cart_page_title_text
        if act_title == exe_title:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("..\\ScreenShots\\test_cart_page_delete_btn.png")
            self.driver.close()
            assert False