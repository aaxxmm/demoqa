from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from pages.form_page import FormPage
import time

def test_modal_elements(browser): #передаём браузер
    form_page = FormPage(browser) #создаём объект страницы \передаём браузер
    form_page.visit()