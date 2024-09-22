from pages.accordion import Accordion
import time

def test_visible_accordion(browser):
    accordion_page = Accordion(browser)
    accordion_page.visit()
    assert accordion_page.lorem_field.visible()
    accordion_page.lorem_btn.click()
    time.sleep(2)
    assert not accordion_page.lorem_field.visible()


def test_visible_accordion_default(browser):
    accordion_page = Accordion(browser)
    accordion_page.visit()
    assert not accordion_page.lorem_btn_1.visible()
    assert not accordion_page.lorem_btn_2.visible()
    assert not accordion_page.lorem_btn_self.visible()
