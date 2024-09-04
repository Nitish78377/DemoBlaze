import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Product_Page:
    """Page Objects"""
    product_page_xpath = "//h4[@class='card-title']//a[text()='Nokia lumia 1520']"
    phones_category_xpath = "//a[@id='itemc' and text()='Phones']"
    laptops_category_xpath = "//a[@id='itemc' and text()='Laptops']"
    monitors_category_xpath = "//a[@id='itemc' and text()='Monitors']"
    product_description_xpath = "//div[@id='myTabContent']//strong"

    laptops_category_product_xpath = "//h4[@class='card-title']//a[text()='Sony vaio i5']"
    monitors_category_product_xpath = "//h4[@class='card-title']//a[text()='Apple monitor 24']"

    product_page_nextbtn_ID = 'next2'
    product_page_nextbtn_product_xpath = "//h4[@class='card-title']//a[text()='MacBook air']"

    product_page_previousbtn_ID = 'prev2'

    add_to_cartbtn_xpath = "//a[text()='Add to cart']"

    def __init__(self, driver):
        self.driver = driver

        """Page Actions"""

    def product_page_visible(self):
        text = self.driver.find_element(By.XPATH, self.product_page_xpath).text
        return text

    def click_product(self):
        self.driver.find_element(By.XPATH, self.product_page_xpath).click()

    def product_description_page(self):
        text = self.driver.find_element(By.XPATH, self.product_description_xpath).text
        return text

    def click_phones_category(self):
        self.driver.find_element(By.XPATH, self.phones_category_xpath).click()

    def click_laptops_category(self):
        self.driver.find_element(By.XPATH, self.laptops_category_xpath).click()

    def click_monitors_category(self):
        self.driver.find_element(By.XPATH, self.monitors_category_xpath).click()

    def laptops_category_product_text(self):
        text = self.driver.find_element(By.XPATH, self.laptops_category_product_xpath).text
        return text

    def monitor_category_product_text(self):
        text = self.driver.find_element(By.XPATH, self.monitors_category_product_xpath).text
        return text

    def click_nextbtn(self):
        self.driver.find_element(By.ID, self.product_page_nextbtn_ID).click()

    def nextbtn_product(self):
        text = self.driver.find_element(By.XPATH, self.product_page_nextbtn_product_xpath).text
        return text

    def click_previousbtn(self):
        self.driver.find_element(By.ID, self.product_page_previousbtn_ID).click()

    def previousbtn_product(self):
        text = self.driver.find_element(By.XPATH, self.product_page_xpath).text
        return text

    def click_addto_cartbtn(self):
        self.driver.find_element(By.XPATH,self.add_to_cartbtn_xpath ).click()
