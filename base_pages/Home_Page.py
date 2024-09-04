import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By


class Home_Page:
    """Page Objects"""
    homePage_text_ID = 'nava'

    def __init__(self, driver):
        self.driver = driver

        """Page Actions"""

    def homepage_text(self):
        home_page_text = self.driver.find_element(By.ID,self.homePage_text_ID).text
        return home_page_text
