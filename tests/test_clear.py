from selenium.common.exceptions import NoSuchElementException
from pages.text_box import TextBox
import time

def test_clear(browser): #передаём браузер
    text_box = TextBox(browser) #создаём объект страницы \передаём браузер
    text_box.visit()
    text_box.name.send_keys('tester')
    time.sleep(2)
    text_box.name.clear()
    time.sleep(2)

    assert text_box.name.get_text() == ''  #эл-т на странице
