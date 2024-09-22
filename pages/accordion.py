from pages.base_page import BasePage
from components.components import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class Accordion(BasePage):  # наследуем от BasePage
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.lorem_field = WebElement(driver, "#section1Content > p")
        self.lorem_btn = WebElement(driver, "#section1Heading")
        self.lorem_btn_1 = WebElement(driver, "#section2Content > p:nth-child(1)")
        self.lorem_btn_2 = WebElement(driver, "#section2Content > p:nth-child(2)")
        self.lorem_btn_self = WebElement(driver, "#section3Content > p")
