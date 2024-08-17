from selenium.webdriver.common.by import By
import time

class BasePage:
   def __init__(self, driver): #после self принимающиеся аргументы
       self.driver = driver
       self.base_url = 'https://demoqa.com/'

   def visit(self):  #метод visit возвращает переход на страницу get
       return self.driver.get(self.base_url)

   def find_element(self, locator):#метод find_element
       time.sleep(3)
       return self.driver.find_element(By.CSS_SELECTOR, locator)

   def get_url(self):
       return self.driver.current_url