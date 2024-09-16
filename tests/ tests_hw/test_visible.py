from pages.base_page import BasePage
from components.components import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from pages.accordion import Accordion
import time

def test_visible_accordion(browser):
    accordion_page = Accordion(browser)
    accordion_page.go_to_page()

    # Тест-кейс ii
    assert accordion_page.SECTION1_CONTENT[1].is_displayed()

    # Тест-кейс iii
    accordion_page.SECTION1_HEADING[1].click()

    # Тест-кейс iv
    time.sleep(2)

    # Тест-кейс v
    assert not accordion_page.SECTION1_CONTENT[1].is_displayed()


def test_visible_accordion_default(browser):
    # Тест-кейс i
    accordion_page = Accordion(browser)
    accordion_page.go_to_page()

    # Тест-кейс ii
    assert not accordion_page.SECTION2_CONTENT_P1[1].is_displayed()
    assert not accordion_page.SECTION2_CONTENT_P2[1].is_displayed()
    assert not accordion_page.SECTION3_CONTENT[1].is_displayed()

#     # Проверка, что элемент #section1Content > p виден
#     assert accordion_page.section1_content().is_displayed() == True
#
#     # Клик на #section1Heading
#     accordion_page.section1_heading().click()
#     time.sleep(2)
#
#     # Проверка, что элемент #section1Content > p НЕ виден
#     assert accordion_page.section1_content().is_displayed() == False
#
#
# def test_visible_accordion_default(browser):
#     accordion_page = Accordion(browser)
#     accordion_page.visit()
#
#     # Проверка, что элементы по умолчанию скрыты
#     assert accordion_page.section2_content_1().is_displayed() == False
#     assert accordion_page.section2_content_2().is_displayed() == False
#     assert accordion_page.section3_content().is_displayed() == False