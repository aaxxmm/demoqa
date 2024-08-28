from selenium.webdriver.common.by import By

class BasePage:
   def __init__(self, driver, base_url): #после self принимающиеся аргументы
       self.driver = driver
       self.base_url = base_url

   def visit(self):  #метод visit возвращает переход на страницу get
       return self.driver.get(self.base_url)
   #
   # def find_element(self, locator):#метод find_element
   #     return self.driver.find_element(By.CSS_SELECTOR, locator)

   def get_url(self):
       return self.driver.current_url

   def equal_url(self):
       if self.get_url() == self.base_url:
           return True
       else:
           return False