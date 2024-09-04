import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Cart_Page:
    """Page Objects"""
    cart_page_delete_btn_xpath = "//tbody[@id='tbodyid']//a[text()='Delete']"



    def __init__(self, driver):
        self.driver = driver

        """Page Actions"""

    def click_on_delete_btn(self):
        self.driver.find_element(By.XPATH,self.cart_page_delete_btn_xpath).click()



