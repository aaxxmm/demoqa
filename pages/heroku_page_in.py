from pages.base_page import BasePage
from components.components import WebElement


class HerokuAppAdd(BasePage):
    def __init__(self, driver):
        self.base_url = 'http://the-internet.herokuapp.com/add_remove_elements/'
        super().__init__(driver, self.base_url)
        self.add_element_btn = WebElement(driver, '#content > div > button')
        self.del_btn_all = WebElement(driver, "//*[@id='elements']/button", 'xpath')
        self.add_element_btn = WebElement(driver, '#content > div > button')
