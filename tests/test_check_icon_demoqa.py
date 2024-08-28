from pages.demoqa import DemoQa
def test_check_icon(browser): #browser-аргумент

    demo_qa_page = DemoQa(browser) #
    demo_qa_page.visit() #посещаем страницу
    demo_qa_page.icon.click()
    assert demo_qa_page.equal_url()
    assert demo_qa_page.exist_icon()  #эл-т есть на странице

