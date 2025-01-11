import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from base.base_class import Base
from selenium.webdriver.common.keys import Keys

#потомок класса Base
class Order_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.driver.implicitly_wait(10)

    #Locators (Создали переменные, в которых храним локаторы)
    make_order = "//h1[contains(text(), 'Оформление заказа')]"
    location = "//input[@class='bx-ui-sls-fake']"
    dropdown_active = "//span[@class ='dropdown-item-text']"
    next_button = "(//div//a[contains(text(),'Далее')])[1]"
    delivery_checkbox = "//input[@id = 'ID_DELIVERY_ID_2']"
    delivery_next_button = "(//div//a[contains(text(),'Далее')])[2]"
    card_checkbox = "//div//input[@id = 'ID_PAY_SYSTEM_ID_8']"
    card_next_button = "(//div//a[contains(text(),'Далее')])[3]"
    full_name = "//input[@id='soa-property-1']"
    email = "//input[@id='soa-property-2']"
    phone = "//input[@id='soa-property-3']"
    info_next_button = "(//div//a[contains(text(),'Далее')])[4]"
    product_1_name_in_order = "//div[@class ='bx-soa-item-title']"
    total_price = "(//div//span[@class='bx-soa-cart-d'])[6]"

    #Getters (в методах просим вернуть явное ожидание WebDriverWait, указываем обязательное условие кликабельности для локатора и указываем к какому локатору обращаемся)
    def get_make_order(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.make_order)))
    def get_location(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.location)))
    def get_dropdown_active(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.dropdown_active)))
    def get_next_button(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.next_button)))
    def get_delivery_checkbox(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.delivery_checkbox)))
    def get_card_checkbox(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.card_checkbox)))
    def get_full_name(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.full_name)))
    def get_email(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.email)))
    def get_phone(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.phone)))
    def get_product_1_name_in_order(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.product_1_name_in_order)))
    def get_total_price(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.total_price)))

    #Actions
    def input_location(self):
        self.get_location().send_keys("Казань")
        self.get_dropdown_active().click()
        print("Location is entered.")
        time.sleep(10)
        self.get_next_button().click()
        print("Click next button.")

    def click_delivery_checkbox(self):
        time.sleep(1)
        self.get_delivery_checkbox().click()
        print("Click delivery checkbox")
        time.sleep(10)
        self.get_next_button().click()
        print("Click next button")
    def click_card_checkbox(self):
        time.sleep(1)
        self.get_card_checkbox().click()
        print("Click card checkbox")
        time.sleep(10)
        self.get_next_button().click()
        print("Click next button")
    def input_info(self):
        time.sleep(1)
        self.get_full_name().send_keys(Keys.CONTROL + 'a')
        self.get_full_name().send_keys("Иванов Иван Иванович")
        print("Input full name.")
        self.get_email().send_keys(Keys.CONTROL + 'a')
        self.get_email().send_keys(self.e_mail)
        self.get_phone().send_keys("89457345693")
        print("Input phone.")
        self.get_next_button().click()
        print("Click next button.")

    #Methos
    def input_order_info(self):
        self.get_current_url()
        self.input_location()
        self.click_delivery_checkbox()
        self.click_card_checkbox()
        self.input_info()

    # Сделать заказ
    # def make_order(self):
    #     self.input_location()






