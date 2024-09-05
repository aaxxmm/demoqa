import time

from pages.elements_page import ElementsPage

# def test_visible_btn_sidebar(browser):
#     elements_pages = ElementsPage(browser)
#
#     elements_pages.visit()
#     elements_pages.btn_sidebar_first.click()
    # time.sleep(3)
    # assert elements_pages.btn_sidebar_first_textbox.exist()
    # assert elements_pages.btn_sidebar_first_textbox.visible()

def test_not_btn_sidebar(browser):
    elements_pages = ElementsPage(browser)

    elements_pages.visit()
    assert elements_pages.btn_sidebar_first_checkbox.visible()
    elements_pages.btn_sidebar_first.click()
    time.sleep(2)
    assert not elements_pages.btn_sidebar_first_checkbox.visible()
