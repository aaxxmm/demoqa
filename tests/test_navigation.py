from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

def test_navigation(browser): #browser-аргумент
    demo_qa_page = DemoQa(browser) #
    elements_page = ElementsPage(browser) #объект

    demo_qa_page.visit() #посещаем страницу
    demo_qa_page.btn_elements.click()

    demo_qa_page.refresh()
    browser.refresh()
    browser.back()
    browser.forward()

    assert elements_page.equal_url()

