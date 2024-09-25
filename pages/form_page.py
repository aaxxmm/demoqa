from components.components import WebElement
from pages.base_page import BasePage

class FormPage(BasePage): #наследуем от BasePage
    def __init__(self, driver): #конструктор класса, метод инит
        self.base_url = 'https://demoqa.com/automation-practice-form' #урл страницы
        super().__init__(driver, self.base_url) #метод супер для вноса изменений и не конфликта базового и род. ур

        self.first_name = WebElement(driver,'#firstName')
        self.last_name = WebElement(driver,'#lastName') #
        self.user_email = WebElement(driver,'#userEmail') #
        self.gender_radio_1 = WebElement(driver,'#gender-radio-1') #
        self.user_number = WebElement(driver,'#userNumber') #
        self.btn_submit = WebElement(driver,'#submit') #кнопка подтверждения
        self.modal_dialog = WebElement(driver,'body > div.fade.modal.show > div') #модальное окно
        self.btn_close_modal = WebElement(driver,'#closeLargeModal') #

        self.hobbies = WebElement(driver, '#hobbies-checkbox-1')  # модальное окно
        self.current_address = WebElement(driver, '#currentAddress')  #
        self.hobbies_check = WebElement(driver, '#hobbies-checkbox-2')
        self.btn_current_address = WebElement(driver,'#currentAddress')
        self.btn_state = WebElement(driver, '#state')
        self.inp_state = WebElement(driver, '#react-select-3-input')
        self.btn_city = WebElement(driver, '#stateCity-wrapper > div:nth-child(3)')
        self.inp_city = WebElement(driver,"//*[contains(text(),'Delhi')]", 'xpath')
        self.btn_state = WebElement(driver, '#state')
        self.inp_state = WebElement(driver, '#react-select-3-input')

        self.btn_NCR = WebElement(driver, "//*[contains(text(),'NCR')]", 'xpath')
