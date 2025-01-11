import datetime
from selenium.webdriver.common.action_chains import ActionChains    #импорт класс ActionChains

#Создаем метод инит и передаем driver экземпляр драйвера хром
class Base():

    def __init__(self, driver, ):
        self.driver = driver
        self.action = ActionChains(self.driver)

    def move_slider(self, slider, x, y):
        self.action.click_and_hold(slider).move_by_offset(x, y).release().perform()

    def scroll_to_element(self, element):
        self.action.move_to_element(element).perform()

    #Method get current url
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    #Method assert word

    def assert_word(self, word, result):
        value_word = word.text
        print(value_word)
        assert value_word == result
        print("Assertion for word passed")

    #Method assert url
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Assertion for url passed")

    e_mail = "vatofroifabeu-9163@yopmail.com"
    pass_word = "forprojectmail65@"
















