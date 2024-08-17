import pytest
from selenium import webdriver


@pytest.fixture(scope="session") #декоратор,обертка,изменяет поведение др функции
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit() #закрыть драйвер