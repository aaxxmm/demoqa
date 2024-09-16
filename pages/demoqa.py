from selenium.common.exceptions import NoSuchElementException   #исключение импортируем
from pages.base_page import BasePage
from components.components import WebElement

class DemoQa(BasePage): #наследуем от BasePage
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver, self.base_url)

        self.icon = WebElement(driver, '#app > header > a')
        self.btn_elements = WebElement(driver, "#app > div > div > div.home-body > div > div:nth-child(1)")
        self.footer_text = WebElement(driver, 'div.col-12.mt-4.col-md-6:nth-child(2)')
        self.center_text = WebElement(driver, 'body:nth-child(2) div:nth-child(6) > div.body-height:nth-child(2)')
        self.text_please = WebElement(driver, '#body:nth-child(2) div:nth-child(6) > footer:nth-child(3)')

        self.text_footer = WebElement(driver, locator='#app > footer > span')
        self.btn_first_d = WebElement(driver, locator='div:nth-child(1) > div > div > div:nth-child(1) > span > div')
        self.text_box_btn_d = WebElement(driver, locator='div:nth-child(1) > div #item-0')