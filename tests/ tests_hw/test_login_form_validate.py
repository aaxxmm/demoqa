from pages.form_page import FormPage
import time


def test_login_form_validate(browser):
    login_form_page = FormPage(browser)
    login_form_page.visit()
    assert login_form_page.first_name.get_dom_attribute('placeholder') == 'First Name'
    assert login_form_page.last_name.get_dom_attribute('placeholder') == 'Last Name'
    assert login_form_page.user_email.get_dom_attribute('placeholder') == 'name@example.com'
    assert login_form_page.user_email.get_dom_attribute('pattern') == '^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$'


    login_form_page.btn_submit.click_force()
    time.sleep(2)
    assert 'was-validated' in login_form_page.user_form.get_dom_attribute('class')