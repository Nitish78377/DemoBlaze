import time
import pytest
from Test_Data.TestData import TestData
from Configurations.basefile import BasePage
from selenium.webdriver.common.by import By
from base_pages.Home_Page import Home_Page
from base_pages.Login_Page import Login_Page
from base_pages.CheckOut_Page import CheckOut_Page
from base_pages.Product_Page import Product_Page


class Test_CheckOut_Page:
    @pytest.mark.sanity
    def test_cartPage_verification(self, setup):
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
        self.cp = CheckOut_Page(self.driver)
        self.cp.click_cart_nav()
        act_title = self.cp.cart_page_title()
        exe_title = TestData.Cart_page_title_text
        if act_title == exe_title:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("..\\ScreenShots\\test_cartPage_verification.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    def test_place_order(self, setup):
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
        time.sleep(3)
        self.cp = CheckOut_Page(self.driver)
        self.cp.click_cart_nav()
        self.cp.click_on_place_order()
        self.cp.enter_name(TestData.Name)
        self.cp.enter_country(TestData.Country)
        self.cp.enter_city(TestData.City)
        self.cp.enter_credit_card(TestData.Credit_Card)
        self.cp.enter_month(TestData.Month)
        self.cp.enter_year(TestData.Year)
        self.cp.click_on_purchase_btn()
        success_message = self.cp.purchase_successfull_message()
        if success_message == TestData.Purchase_Successfull_text:
            assert True
            self.cp.click_on_Purchase_ok_btn()
            self.driver.close()
        else:
            self.driver.save_screenshot("..\\ScreenShots\\test_place_order.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    def test_place_order_close_btn(self, setup):
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
        time.sleep(3)
        self.cp = CheckOut_Page(self.driver)
        self.cp.click_cart_nav()
        self.cp.click_on_place_order()
        self.cp.enter_name(TestData.Name)
        self.cp.enter_country(TestData.Country)
        self.cp.enter_city(TestData.City)
        self.cp.enter_credit_card(TestData.Credit_Card)
        self.cp.enter_month(TestData.Month)
        self.cp.enter_year(TestData.Year)
        self.cp.click_on_purchase_close_btn()
        cart_page_title = self.cp.cart_page_title()
        if cart_page_title == TestData.Cart_page_title_text:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("..\\ScreenShots\\test_place_order_close_btn.png")
            self.driver.close()
            assert False
