from selenium.common.exceptions import NoSuchElementException   #исключение импортируем
from pages.base_page import BasePage
from components.components import WebElement

class DemoQa(BasePage): #наследуем от BasePage
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver, self.base_url)

        self.icon = WebElement(driver, '#app > header > a')
        self.btn_elements = WebElement(driver, "#app > div > div > div.home-body > div > div:nth-child(1)")
    def exist_icon(self): # метод
        try:    #конструкция
            self.icon.find_element()
        except NoSuchElementException:   #исключение
            return False
        return True

