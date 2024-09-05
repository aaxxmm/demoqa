from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
class WebElement:
   def __init__(self,driver, locator=''):
        self.locator = locator
        self.driver = driver

   def click(self):  #
       self.find_element().click() #обращаемся к драйверу,находим элемент,поиск по CSS SELECTOR и в качестве селектора передаём локатор получающий объекты Web Element,метод click


   def find_element(self): #метод find_element
       return self.driver.find_element(By.CSS_SELECTOR, self.locator)

   def exist(self): # метод
        try:    #конструкция
            self.find_element()
        except NoSuchElementException:   #исключение
            return False
        return True

   def get_text(self):
       return str(self.find_element().text)

   def visible(self):
       return self.find_element().is_displayed()


