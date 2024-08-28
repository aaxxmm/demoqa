from selenium.webdriver.common.by import By
class WebElement:
   def __init__(self,driver, locator=''):
        self.driver = driver
        self.locator = locator

   def click_find_element(self):  #
       self.driver.find_element().click() #обращаемся к драйверу,находим элемент,поиск по CSS SELECTOR и в качестве селектора передаём локатор получающий объекты Web Element,метод click


   def find_element(self):#метод find_element
       return self.driver.find_element(By.CSS_SELECTOR, self.locator)
