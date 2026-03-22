from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")
    
    def fill_form(self, first_name, last_name, postal_code):
        """Заполнить форму данными"""
        first = self.driver.find_element(*self.first_name_input)
        first.clear()
        first.send_keys(first_name)
        
        last = self.driver.find_element(*self.last_name_input)
        last.clear()
        last.send_keys(last_name)
        
        postal = self.driver.find_element(*self.postal_code_input)
        postal.clear()
        postal.send_keys(postal_code)
    
    def click_continue(self):
        """Нажать кнопку Continue"""
        button = self.driver.find_element(*self.continue_button)
        button.click()
    
    def get_total(self):
        """Получить итоговую сумму"""
        total_element = self.driver.find_element(*self.total_label)
        total_text = total_element.text
        return total_text.split(": ")[1]
    