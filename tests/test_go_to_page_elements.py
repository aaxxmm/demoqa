from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
def test_go_to_page_elements(browser): #browser-аргумент
    demo_qa_page = DemoQa(browser) #
    elements_page = ElementsPage(browser) #объект

    demo_qa_page.visit() #посещаем страницу
    assert demo_qa_page.equal_url()
    demo_qa_page.btn_elements.click()
    assert elements_page.equal_url()
