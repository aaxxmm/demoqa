from components.components import WebElement
from pages.base_page import BasePage

class FormPage(BasePage): #наследуем от BasePage
    def __init__(self,driver): #конструктор класса, метод инит
        self.base_url = 'https://demoqa.com/automation-practice-form' #урл страницы
        super().__init__(driver, self.base_url) #метод супер для вноса изменений и не конфликта базового и род. ур

        self.first_name = WebElement(driver,'#firstName')
        self.last_n