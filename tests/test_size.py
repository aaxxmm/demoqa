from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
def test_size(browser): #browser-аргумент
    demo_qa_page = DemoQa(browser) #

    demo_qa_page.visit() #посещаем страницу
    browser.set_window_size(1000,300)
    time.sleep(2)
    browser.set_window_size(1000,1000)
