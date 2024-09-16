import pytest
from selenium import webdriver


@pytest.fixture(scope="session") #декоратор,обертка,изменяет поведение др функции
def browser():
    driver = webdriver.Chrome()
    driver.set_window_size(width=1000,height=1000)
    yield driver
    driver.quit() #закрыть драйвер