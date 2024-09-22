from selenium.webdriver.common.by import By

class BasePage:
   def __init__(self, driver, base_url): #после self принимающиеся аргументы
       self.driver = driver
       self.base_url = base_url # 'https://demoqa.com/'

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

   def back(self):
       self.driver.back()

   def forward(self):
       self.driver.forward()
   def refresh(self):
       self.driver.refresh()
   def get_title(self):
       return self.driver.title

   def alert(self):
        try:
            return self.driver.switch_to.alert
        except Exception as ex:
            logging.log(1, ex)
            return False

