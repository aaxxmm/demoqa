from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

class WebElement:
   def __init__(self,driver, locator='', locator_type='css'):
        self.locator = locator
        self.driver = driver
        self.locator_type = locator_type

   def click(self):  #
       self.find_element().click() #обращаемся к драйверу,находим элемент,поиск по CSS SELECTOR и в качестве селектора передаём локатор получающий объекты Web Element,метод click

   def click_force(self):  # метод
       self.driver.execute_script("arguments[0].click();", self.find_element())  #позвл добавлять код для клиент браузера

   def find_element(self): #метод find_element
       return self.driver.find_element(By.CSS_SELECTOR, self.locator)

   def find_elements(self):  # метод find_elements
       return self.driver.find_elements(By.CSS_SELECTOR, self.locator)

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

   def check_count_elements(self, count: int) -> bool: # метод
        if len(self.find_elements()) == count:
            return True
        return False

   def send_keys(self, text: str): # метод
        self.find_element().send_keys(text)

   def clear(self): # метод
        self.find_element().send_keys(Keys.CONTROL + 'a')
        self.find_element().send_keys(Keys.DELETE)



