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

   def back(self):
       self.driver.back()

   def forward(self):
       self.driver.forward()
   def refresh(self):
       self.driver.refresh()
   def get_title(self):
       self.driver.title()

   def test_check_footer_text(self):
       self.driver.get('https://demoqa.com')
       footer_text = self.find_element.footer.get_text()
       assert footer_text == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'

   def test_check_center_text(self):
       self.driver.get('https://demoqa.com')
       self.components.button.click()
       center_text = self.components.center_text.get_text()
       assert center_text == 'Please select an item from left to start practice.'
