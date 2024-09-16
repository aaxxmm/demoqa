from pages.elements_page import ElementsPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By



def test_find_elements(browser): #передаём браузер
    elements_pages = ElementsPage(browser) #создаём обект страницы эл-пейдж\передаём браузер
    elements_pages.visit()

    assert elements_pages.btns_first_menu.check_count_elements(count=9)
