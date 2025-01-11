from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from base.base_class import Base


#потомок класса Base
class Main_page(Base):

    url = 'https://atlant-kazan.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators (Создали переменные, в которых храним локаторы)
    catalog_link = "//li//a[contains(text(),'Каталог')]"
    about_link = "//li//a[contains(text(),'О компании')]"
    news_link = "//li//a[contains(text(),'Новости')]"
    delivery_link = "//li//a[contains(text(),'Доставка и оплата')]"
    service_link = "//li//a[contains(text(),'Гарантия и Сервис')]"
    cooperation_link = "//li//a[contains(text(),'Опт')]"
    stores_link = "//li//a[contains(text(),'Магазины')]"
    stocks_link = "//li//a[contains(text(),'Акции')]"

    #Getters (в методах просим вернуть явное ожидание WebDriverWait, указываем обязательное условие кликабельности для локатора и указываем к какому локатору обращаемся)
    def get_catalog_link(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.catalog_link)))
    def get_about_link(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.about_link)))
    def get_news_link(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.news_link)))
    def get_delivery_link(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.catalog_link)))
    def get_service_link(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.service_link)))
    def get_cooperation_link(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.cooperation_link)))
    def get_stores_link(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.stores_link)))
    def get_stocks_link(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.stocks_link)))

    #Actions
    def click_catalog_link(self):
        self.get_catalog_link().click()
        print("Click catalog link")
    def click_about_link(self):
        self.get_about_link().click()
        print("Click about link")
    def click_news_link(self):
        self.get_news_link().click()
        print("Click news link")
    def click_delivery_link(self):
        self.get_delivery_link().click()
        print("Click delivery link")
    def click_service_link(self):
        self.get_service_link().click()
        print("Click service link")
    def click_cooperation_link(self):
        self.get_cooperation_link().click()
        print("Click cooperation link")
    def click_stores_link(self):
        self.get_stores_link().click()
        print("Click stores link")
    def click_stocks_link(self):
        self.get_stocks_link().click()
        print("Click stocks link")
    #Methos
    def redirect_to_catalog(self):
        # self.driver.get(self.url)
        # self.driver.maximize_window()
        self.get_current_url()
        self.click_catalog_link()








