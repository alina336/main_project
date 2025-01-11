import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from base.base_class import Base


#потомок класса Base
class Login_page(Base):

    url = 'https://atlant-kazan.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators (Создали переменные, в которых храним локаторы)
    open_auth_link = "//a[@class='bx_login_top_inline_link']"
    user_name = "//input[@name='USER_LOGIN']"
    password = "//input[@name='USER_PASSWORD']"
    login_button = "//input[@name='Login']"
    enter_word = "//p[@class='notetext']"
    main_p = "//a[contains (text(), 'Вернуться на главную страницу')]"

    #Getters (в методах просим вернуть явное ожидание WebDriverWait, указываем обязательное условие кликабельности для локатора и указываем к какому локатору обращаемся)
    def get_open_auth_link(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.open_auth_link)))
    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.user_name)))
    def get_password(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.password)))
    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.login_button)))
    def get_enter_word(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.enter_word)))

    def get_main_p(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.main_p)))

    #Actions
    def click_open_auth_link(self):
        self.get_open_auth_link().click()
        print("Click user button")
    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")

    def click_main_p(self):
        self.get_main_p().click()
        print("Click main page link")

    #Methos
    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.click_open_auth_link()
        self.input_user_name(self.e_mail)
        self.input_password(self.pass_word)
        self.click_login_button()
        self.assert_word(self.get_enter_word(), 'Вы зарегистрированы и успешно авторизовались.')
        self.click_main_p()




