from pages.demoqa import DemoQa
import time
def test_check_icon(browser): #browser-аргумент

    demo_qa_page = DemoQa(browser) #
    demo_qa_page.visit() #посещаем страницу
    time.sleep(3)
    demo_qa_page.click_on_the_icon()
    time.sleep(3)
    assert demo_qa_page.equal_url()
    assert demo_qa_page.exist_icon()  #эл-т есть на странице

