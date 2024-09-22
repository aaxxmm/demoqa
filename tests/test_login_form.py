from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
from pages.form_page import FormPage
# def test_login_form(browser): #передаём браузер
#     form_page = FormPage(browser) #создаём объект страницы \передаём браузер
#     form_page.visit()
#
#     assert not form_page.modal_dialog.exist()  #эл-т нет на странице
#     time.sleep(2)
#     form_page.first_name.send_keys('tester')
#     form_page.last_name.send_keys('testerovich')
#     form_page.user_email.send_keys('test@mail.ru')
#     form_page.gender_radio_1.click_force()
#     form_page.user_number.send_keys('1111111111')
#     form_page.hobbies.click_force()
#     form_page.current_address.send_keys('test@mail.com')
#     time.sleep(2)
#     form_page.btn_submit.click_force()
#     time.sleep(2)
#
#     assert form_page.modal_dialog.exist()
#     form_page.btn_close_modal.click_force()

from selenium import webdriver
def test_fill_state_city(browser):
    form_page = FormPage(browser)

    form_page.visit()
    time.sleep(2)
    form_page.btn_state.scroll_to_element()
    form_page.btn_state.click_force()
    form_page.btn_NCR.click()
    time.sleep(2)
