import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains    #импорт класс ActionChains
from base.base_class import Base

#потомок класса Base
class Fridges_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators (Создали переменные, в которых храним локаторы)
    left_slider = "//a[@class='bx-ui-slider-handle left']"
    right_slider = "//a[@class='bx-ui-slider-handle right']"
    pozis_checkbox = "//input[@id='arrFilter_8813_3999108400']"
    type_filter = "//span[contains(text(), 'Тип')]"
    type_checkbox = "//input[@id = 'arrFilter_8814_1730025933']"
    height_filter = "//span[contains(text(), 'Высота')]"
    height_150_checkbox = "//input[@id = 'arrFilter_8849_831161727']"
    submit_button = "//input[@class = 'btn btn-themes']"
    catalog = "//li[@class='bxr-color-flat bxr-title-menu-hover']"
    add_to_cart_1 = "(//button[@class = 'tocart wide cart-btn-atl'])[1]"
    price_product_1_in_catalog = "(//span[@class = 'catalog-new-item-price-big'])[1]"
    enter_cart = "//div[@class='fixed-panel-item fixed-panel-cart']"
    product_1_name_in_catalog = "(//a[@class='catalog-new-item-link'])[1]"

    #Getters (в методах просим вернуть явное ожидание WebDriverWait, указываем обязательное условие кликабельности для локатора и указываем к какому локатору обращаемся)
    def get_left_slider(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.left_slider)))
    def get_right_slider(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.right_slider)))
    def get_pozis_checkbox(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.pozis_checkbox)))
    def get_type_checkbox(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.type_checkbox)))
    def get_type_filter(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.type_filter)))
    def get_height_filter(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.height_filter)))
    def get_height_150_checkbox(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.height_150_checkbox)))
    def get_submit_button(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.submit_button)))
    def get_catalog(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.catalog)))
    def get_add_to_cart_1(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.add_to_cart_1)))
    def get_price_product_1_in_catalog(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.price_product_1_in_catalog)))
    def get_enter_cart(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.enter_cart)))
    def get_product_1_name_in_catalog(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.product_1_name_in_catalog)))


    #Actions
    def move_left_slider(self):
        self.move_slider(self.get_left_slider(), 50, 0)
        print("Move left slider")
    def move_right_slider(self):
        time.sleep(1)
        self.move_slider(self.get_right_slider(), -150, 0)
        print("Move right slider")
    def select_pozis_checkbox(self):
        self.get_pozis_checkbox().click()
        print("Click POZIS checkbox")
    def open_type_filter(self):
        self.get_type_filter().click()
        print("Open type filter")
    def select_type_checkbox(self):
        self.get_type_checkbox().click()
        print("Click type  checkbox")

    def open_height_filter(self):
        self.driver.execute_script("window.scrollTo(0, 400);")
        self.get_height_filter().click()
        print("Open type filter")
    def select_height_150_checkbox(self):
        self.get_height_150_checkbox().click()
        print("Click height from 150 to 200 checkbox")
    def click_submit_button(self):
        self.get_submit_button().click()
        print("Click submit button")
    def scroll_to_catalog(self):
        self.scroll_to_element(self.get_catalog())
    def click_add_to_cart_1(self):
        self.driver.execute_script("window.scrollTo(0, 500);")
        self.get_add_to_cart_1().click()
        print("Click add to cart.")
    def click_enter_cart(self):
        self.get_enter_cart().click()
        print("Click enter to cart")

    #Methos
    def set_filters(self):
        self.get_current_url()
        self.move_left_slider()
        self.move_right_slider()
        self.select_pozis_checkbox()
        self.open_type_filter()
        self.select_type_checkbox()
        self.open_height_filter()
        self.select_height_150_checkbox()
        self.scroll_to_catalog()
        self.click_submit_button()
    def select_product(self):
        self.click_add_to_cart_1()
    def enter_to_cart(self):
        self.click_enter_cart()
