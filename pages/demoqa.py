from selenium.common.exceptions import NoSuchElementException   #исключение импортируем
from pages.base_page import BasePage

class DemoQa(BasePage): #наследуем от BasePage
    def exist_icon(self): # метод
        try:    #конструкция
            self.find_element(locator='#app > header > a')
        except NoSuchElementException:   #исключение
            return False
        return True
    def click_on_the_icon(self):
        self.find_element(locator='#app > header > a').click()
    def equal_url(self):
        if self.get_url() == 'https://demoqa.com/':
            return True
        else:
            return False

