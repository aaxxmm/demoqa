from pages.base_page import BasePage
from components.components import WebElement


class HerokuApp(BasePage):
    def __init__(self, driver):
        self.base_url = 'http://the-internet.herokuapp.com/'
        super().__init__(driver, self.base_url)
        self.add_remove_link = WebElement(driver, '#content > ul > li:nth-child(2) > a')
        self.link_add = WebElement(driver,
                                   'div.row:nth-child(2) div.large-12.columns:nth-child(2) ul:nth-child(4) li:nth-child(2) > a:nth-child(1)')