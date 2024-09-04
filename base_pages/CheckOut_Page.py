import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By


class CheckOut_Page:
    """Page Objects"""
    cartLink_ID = 'cartur'
    cart_page_title_xpath = "//div[@id='page-wrapper']//h2[text()='Products']"
    place_order_xpath = "//button[text()='Place Order']"
    place_order_name_field_ID = 'name'
    place_order_country_field_ID = 'country'
    place_order_city_field_ID = 'city'
    place_order_credit_card_field_ID = 'card'
    place_order_month_field_ID = 'month'
    place_order_year_field_ID = 'year'
    close_btn_xpath = "//div[@id='orderModal']//button[text()='Close']"
    purchase_btn_xpath = "//button[text()='Purchase']"
    purchase_succesfull_message_xpath = "//h2[text()='Thank you for your purchase!']"
    purchase_message_ok_btn_xpath = "//button[text()='OK']"

    def __init__(self, driver):
        self.driver = driver

        """Page Actions"""

    def click_cart_nav(self):
        self.driver.find_element(By.ID, self.cartLink_ID).click()

    def cart_page_title(self):
        text = self.driver.find_element(By.XPATH, self.cart_page_title_xpath).text
        return text

    def click_on_place_order(self):
        self.driver.find_element(By.XPATH, self.place_order_xpath).click()

    def enter_name(self, name):
        self.driver.find_element(By.ID, self.place_order_name_field_ID).send_keys(name)

    def enter_country(self, country):
        self.driver.find_element(By.ID, self.place_order_country_field_ID).clear()
        self.driver.find_element(By.ID, self.place_order_country_field_ID).send_keys(country)

    def enter_city(self, city):
        self.driver.find_element(By.ID, self.place_order_city_field_ID).clear()
        self.driver.find_element(By.ID, self.place_order_city_field_ID).send_keys(city)

    def enter_credit_card(self, card):
        self.driver.find_element(By.ID, self.place_order_credit_card_field_ID).clear()
        self.driver.find_element(By.ID, self.place_order_credit_card_field_ID).send_keys(card)

    def enter_month(self, month):
        self.driver.find_element(By.ID, self.place_order_month_field_ID).clear()
        self.driver.find_element(By.ID, self.place_order_month_field_ID).send_keys(month)

    def enter_year(self, year):
        self.driver.find_element(By.ID, self.place_order_year_field_ID).clear()
        self.driver.find_element(By.ID, self.place_order_year_field_ID).send_keys(year)

    def click_on_purchase_btn(self):
        self.driver.find_element(By.XPATH, self.purchase_btn_xpath).click()

    def purchase_successfull_message(self):
        successMessage = self.driver.find_element(By.XPATH, self.purchase_succesfull_message_xpath).text
        return successMessage

    def click_on_Purchase_ok_btn(self):
        self.driver.find_element(By.XPATH, self.purchase_message_ok_btn_xpath).click()

    def click_on_purchase_close_btn(self):
        self.driver.find_element(By.XPATH,self.close_btn_xpath).click()
