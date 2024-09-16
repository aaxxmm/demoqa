from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage

def test_check_footer(browser): #browser-аргумент

    demo_qa_page = DemoQa(browser) #
    demo_qa_page.visit() #посещаем страницу
    assert demo_qa_page.footer_text.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'
    demo_qa_page.btn_elements.click()
    el_page = ElementsPage(browser)
    assert el_page.text_center_elements.get_text() == 'Please select an item from left to start practice.'

# def test_page_elements(browser):
#
#     elem_page = ElementsPage(browser)
#     elem_page.visit()
#     assert elem_page.text_elements.get_text() == 'Please select an item from left to start practice.'
#   assert elem_page.icon.exist()
  #  assert elem_page.btn_siebar_first.exist()
 #   assert elem_page.btn_siebar_first_textbox.exist()