from pages.heroku_page import HerokuApp
from pages.heroku_page_in import HerokuAppAdd


def test_btn_add(browser):
    hero_page = HerokuApp(browser)
    hero_page_add = HerokuAppAdd(browser)
    hero_page.visit()
    assert hero_page.add_remove_link.exist()
    hero_page.add_remove_link.click()
    assert hero_page_add.equal_url()
    assert hero_page_add.add_element_btn.exist()
    assert hero_page_add.add_element_btn.get_dom_attribute('onclick') == "addElement()"

    for i in range(4):
        hero_page_add.add_element_btn.click()
    assert hero_page_add.del_btn_all.check_count_elements(4)

    for elem in hero_page_add.del_btn_all.find_elements():
        assert elem.text == 'Delete'

    while hero_page_add.del_btn_all.exist():
        hero_page_add.del_btn_all.click()

    assert not hero_page_add.del_btn_all.exist()