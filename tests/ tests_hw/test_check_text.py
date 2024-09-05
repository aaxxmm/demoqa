from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

# def test_check_footer(browser): #browser-аргумент
#
#     demo_qa_page = DemoQa(browser) #
#     demo_qa_page.visit() #посещаем страницу
#     assert demo_qa_page.footer_text.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'
#
# def test_check_text_center(browser):  # browser-аргумент
#
#     demo_qa_page = DemoQa(browser)  #
#     el_page = ElementsPage(browser)
#
#     demo_qa_page.visit()  # посещаем страницу
#     demo_qa_page.btn_elements.click()
#     assert el_page.center_text.text_please.get_text() == 'Please select an item from left to start practice.'

def test_page_elements(browser):
    el_page = ElementsPage(browser)

    el_page.visit()
    # assert el_page.text_elements.get_text() == 'Please select an item from left to start practice.'
    assert el_page.icon.exist()
    assert el_page.btn_siebar_first.exist()
    assert el_page.btn_siebar_first_textbox.exist()