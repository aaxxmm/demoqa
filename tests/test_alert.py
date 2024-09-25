from pages.alerts import Alerts
import time

# def test_alert(browser):
# проверка видимости алерта
#     alert_page = Alerts(browser)
#
#     alert_page.visit()
#     assert not alert_page.alert()
#
#     alert_page.alert_button.click()
#     time.sleep(2)
#     assert alert_page.alert()

# def test_alert_text(browser):
#  подтверждение алерта
#       alert_page = Alerts(browser)
#
#       alert_page.visit()
#       alert_page.alert_button.click()
#       assert alert_page.alert().text == 'You clicked a button'
#
#       alert_page.alert().accept()
#       assert not alert_page.alert()


# def test_alert_confirm(browser):
#       #отмена алерта
#       page_alerts = Alerts(browser)
#       page_alerts.visit()
#
#       page_alerts.confirm_button.click()
#       time.sleep(2)
#       page_alerts.alert().dismiss()
#
#       assert page_alerts.confirm_result.get_text() == 'You selected Cancel'

def  test_alert_prompt(browser):
      #введеное слово
      page_alerts = Alerts(browser)
      name = 'Max'
      page_alerts.visit()

      page_alerts.prompt_button.click()
      time.sleep(2)
      page_alerts.alert().send_keys(name)
      page_alerts.alert().accept() #нажали кнопку окей
      assert page_alerts.prompt_result.get_text() == 'You entered { name }'




