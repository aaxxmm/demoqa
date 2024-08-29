from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
class ElementsPage(BasePage): #наследуем от BasePage
    def __init__(self,driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver, self.base_url)
