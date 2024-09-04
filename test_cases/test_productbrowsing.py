import time
import pytest
from Test_Data.TestData import TestData
from Configurations.basefile import BasePage
from selenium.webdriver.common.by import By
from base_pages.Home_Page import Home_Page
from base_pages.Login_Page import Login_Page
from base_pages.CheckOut_Page import CheckOut_Page
from base_pages.Product_Page import Product_Page


class Test_Product_Page:
    @pytest.mark.sanity
    def test_productPage_verification(self, setup):
        self.driver = setup
        self.driver.get(BasePage.Page_url)
        time.sleep(2)
        self.pp = Product_Page(self.driver)
        act_title = self.pp.product_page_visible()
        exe_title = TestData.Product_text
        if act_title == exe_title:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("..\\ScreenShots\\test_productPage_verification.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    def test_productPage_Phones_categories(self, setup):
        self.driver = setup
        self.driver.get(BasePage.Page_url)
        time.sleep(2)
        self.pp = Product_Page(self.driver)
        self.pp.click_phones_category()
        time.sleep(3)
        act_title = self.pp.product_page_visible()
        exe_title = TestData.Product_text
        if act_title == exe_title:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("..\\ScreenShots\\test_productPage_Phones_categories.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    def test_productPage_Laptops_category(self, setup):
        self.driver = setup
        self.driver.get(BasePage.Page_url)
        time.sleep(2)
        self.pp = Product_Page(self.driver)
        self.pp.click_laptops_category()
        time.sleep(3)
        act_title = self.pp.laptops_category_product_text()
        exe_title = TestData.Laptops_category_product_text
        if act_title == exe_title:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("..\\ScreenShots\\test_productPage_Laptops_category.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    def test_productPage_Monitors_category(self, setup):
        self.driver = setup
        self.driver.get(BasePage.Page_url)
        time.sleep(2)
        self.pp = Product_Page(self.driver)
        self.pp.click_monitors_category()
        time.sleep(3)
        act_title = self.pp.monitor_category_product_text()
        exe_title = TestData.Monitors_category_product_text
        if act_title == exe_title:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("..\\ScreenShots\\test_productPage_Monitors_category.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    def test_productPage_nextbtn_pagination(self, setup):
        self.driver = setup
        self.driver.get(BasePage.Page_url)
        time.sleep(2)
        self.pp = Product_Page(self.driver)
        self.pp.click_nextbtn()
        time.sleep(3)
        act_title = self.pp.nextbtn_product()
        exe_title = TestData.NextBtn_Product_text
        if act_title == exe_title:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("..\\ScreenShots\\test_productPage_nextbtn_pagination.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    def test_productPage_previousbtn_pagination(self, setup):
        self.driver = setup
        self.driver.get(BasePage.Page_url)
        time.sleep(2)
        self.pp = Product_Page(self.driver)
        self.pp.click_nextbtn()
        time.sleep(3)
        self.pp.click_previousbtn()
        act_title = self.pp.previousbtn_product()
        exe_title = TestData.Product_text
        if act_title == exe_title:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("..\\ScreenShots\\test_productPage_previousbtn_pagination.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    def test_product_description_page(self, setup):
        self.driver = setup
        self.driver.get(BasePage.Page_url)
        time.sleep(2)
        self.pp = Product_Page(self.driver)
        self.pp.click_product()
        time.sleep(3)
        act_title = self.pp.product_description_page()
        exe_title = TestData.product_description_page_text
        if act_title == exe_title:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("..\\ScreenShots\\test_product_description_page.png")
            self.driver.close()
            assert False
