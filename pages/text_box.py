from selenium.common.exceptions import NoSuchElementException  # исключение импортируем
from pages.base_page import BasePage
from components.components import WebElement


class TextBox(BasePage):  # наследуем от BasePage
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)

        self.name = WebElement(driver, 'userName')
        self.full_name = WebElement(driver, '#userName')
        self.placeholder_btn = WebElement(driver, '#userName')
        self.current_address = WebElement(driver,'#currentAddress-wrapper>div>#currentAddress')
        self.submit_btn = WebElement(driver, '#submit')
        self.output_name = WebElement(driver, '#name')
        self.output_address = WebElement(driver, '#output > div > #currentAddress')
        self.output_elements = WebElement(driver, '#output > div >p')

