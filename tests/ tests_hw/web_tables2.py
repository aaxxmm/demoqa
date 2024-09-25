import time
from pages.web_tables import Tables


def test_add_submit_form(browser):
    page_tables = Tables(browser)
    page_tables.visit()

    page_tables.btn_add.click()
    assert page_tables.reg_form.exist()

    page_tables.btn_submit.click()
    assert page_tables.reg_form.exist()
    time.sleep(2)

    page_tables.first_name_field.send_keys('Malder')
    page_tables.last_name_field.send_keys('Fox')
    page_tables.email_field.send_keys('email@gmail.com')
    page_tables.age_field.send_keys('30')
    page_tables.salary_field.send_keys('1000')
    page_tables.department_field.send_keys('Police')
    page_tables.btn_submit.click()
    time.sleep(2)
    assert page_tables.string_exist.get_text() == 'Malder'

    page_tables.edit_record.click()
    page_tables.first_name_field.clear()
    page_tables.first_name_field.send_keys('Scally')
    page_tables.btn_submit.click()
    time.sleep(2)
    assert page_tables.string_exist.get_text() == 'Scally'
    time.sleep(2)

    page_tables.delete_record.click()
    assert page_tables.string_exist.get_text() == ' '
    time.sleep(2)


def test_next_previous(browser):
    page_tables = Tables(browser)
    page_tables.visit()

    page_tables.select_row.scroll_to_element()
    page_tables.select_row.click()
    page_tables.establish_5row.click()
    time.sleep(2)

    for i in range(3):
        page_tables.btn_add.click()
        page_tables.first_name_field.send_keys('Maykl')
        page_tables.last_name_field.send_keys('Lis')
        page_tables.email_field.send_keys('email@gmail.com')
        page_tables.age_field.send_keys('31')
        page_tables.salary_field.send_keys('1000')
        page_tables.department_field.send_keys('Driver')
        page_tables.btn_submit.click()
        time.sleep(3)

    assert page_tables.string_exist.get_text() == 'Maykl'

    page_tables.btn_next.click()
    time.sleep(2)

    assert page_tables.page_num.get_dom_attribute('value') == '2'

    page_tables.btn_previous.click()
    time.sleep(2)

    assert page_tables.page_num.get_dom_attribute('value') == '1'

