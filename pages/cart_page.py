from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from base.base_class import Base
import pages.fridges_catalog_page


#потомок класса Base
class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators (Создали переменные, в которых храним локаторы)
    checkout_button = "//a[@class='checkout']"
    product_1_name_in_cart = "//h2[@class='bx_ordercart_itemtitle']"
    quantity = "//td//input[@type='text']"
    product_1_price_in_cart = "//div[@class='current_price']"


    #Getters (в методах просим вернуть явное ожидание WebDriverWait, указываем обязательное условие кликабельности для локатора и указываем к какому локатору обращаемся)
    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.checkout_button)))
    def get_product_1_name_in_cart(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.product_1_name_in_cart)))
    def get_product_1_price_in_cart(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.product_1_price_in_cart)))
    def get_quantity(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.quantity)))

    #Actions

    def click_checkout_button(self):
        self.driver.execute_script("window.scrollTo(0, 300);")
        self.get_checkout_button().click()
        print("Click checkout button")
    def input_quantity(self):
        self.get_quantity().send_keys(Keys.CONTROL + 'a')
        self.get_quantity().send_keys('1')
    #Methos
    def product_confirmation(self):
        self.get_current_url()
        self.input_quantity()
        self.click_checkout_button()


