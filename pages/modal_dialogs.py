from components.components import WebElement
from pages.base_page import BasePage

class ModalDialogs(BasePage): #наследуем от BasePage
    def __init__(self,driver): #конструктор класса, метод инит
        self.base_url = 'https://demoqa.com/modal-dialogs' #урл страницы
        super().__init__(driver, self.base_url) #метод супер для вноса изменений и не конфликта базового и род. ур

        self.btns_all = WebElement(driver, ' div:nth-child(3) > div > ul > li')
        self.icon_btn = WebElement(driver, '#app > header > a')
        self.small_modal = WebElement(driver, '#showSmallModal')
        self.large_modal = WebElement(driver, '#showLargeModal')
        self.close_small_modal = WebElement(driver, '#closeSmallModal')
        self.close_large_modal = WebElement(driver, '#closeLargeModal')
