from pages.demoqa import DemoQa
from pages.accordion import Accordion
from pages.alerts import Alerts
from pages.browser_tab import BrowserTab

import pytest
import time

def test_seo(browser): #browser-аргумент
    demo_qa_page = DemoQa(browser) #

    demo_qa_page.visit() #посещаем страницу
    assert browser.title == 'DEMOQA'



@pytest.mark.parametrize("pages", [Accordion, Alerts, DemoQa, BrowserTab]) #декоратор, помогает циклично тестировать
# несколько страниц
def test_check_title_all_pages(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)
    assert page.get_title() == 'DEMOQA'


