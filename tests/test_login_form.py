from pages.form_page import FormPage
import time


def test_login_form(browser):
    form_page = FormPage(browser)
    form_page.visit()
    assert not form_page.modal_dialog.exist()
    time.sleep(2)
    form_page.first_name.send_keys("Malder")
    form_page.last_name.send_keys("Foxi")
    form_page.user_email.send_keys("test@gmail.com")
    form_page.gender_radio_1.click_force()
    form_page.user_number.send_keys("1111111111")
    time.sleep(2)
    form_page.btn_submit.click_force()
    time.sleep(2)
    assert form_page.modal_dialog.exist()
    form_page.btn_close_modal.click_force()
    form_page.hobbies_check.click_force()
    form_page.btn_current_address.send_keys("Moscow")
    time.sleep(2)

def test_fill_state_city(browser):
    fill_page = FormPage(browser)
    fill_page.visit()
    fill_page.btn_state.click_force()
    fill_page.inp_state.send_keys('NCR')
    fill_page.inp_state.ent()
    fill_page.btn_city.click()
    fill_page.inp_city.click()
