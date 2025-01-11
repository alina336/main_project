from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from base.base_class import Base


#потомок класса Base
class Catalog_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators (Создали переменные, в которых храним локаторы)
    fridges_catalog_link = "(//a[contains(text(),'Холодильники')])[4]"


    #Getters (в методах просим вернуть явное ожидание WebDriverWait, указываем обязательное условие кликабельности для локатора и указываем к какому локатору обращаемся)
    def get_fridges_catalog_link(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.fridges_catalog_link)))

    #Actions
    def click_fridges_catalog_link(self):
        self.get_fridges_catalog_link().click()
        print("Click fridges catalog link")

    #Methos
    def redirect_fridges_catalog(self):
        self.get_current_url()
        self.click_fridges_catalog_link()








