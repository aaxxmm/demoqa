import time
from pages.alerts import Alerts

def test_check_alert(browser):
    page_alerts = Alerts(browser)
    page_alerts.visit()

    page_alerts.timer_alert_button.click()
    time.sleep(5)
    assert page_alerts.alert()

    page_alerts.alert().accept()
    assert not page_alerts.alert()