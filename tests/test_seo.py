from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

def test_seo(browser): #browser-аргумент
    demo_qa_page = DemoQa(browser) #

    demo_qa_page.visit() #посещаем страницу
    assert browser.title == 'DEMOQA'


