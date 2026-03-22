from selenium.webdriver.common.by import By
import time

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.ID, "delay")
        self.result_field = (By.CLASS_NAME, "screen")
    
    def open(self, url):
        self.driver.get(url)
    
    def set_delay(self, seconds):
        delay_element = self.driver.find_element(*self.delay_input)
        delay_element.clear() 
        delay_element.send_keys(str(seconds))  
    
    def click_button(self, button_text):
        button = self.driver.find_element(By.XPATH, f"//span[text()='{button_text}']")
        button.click()

    def click_sequence(self, buttons):
        for button in buttons:
            self.click_button(button)
    
    def get_result(self):
        result_element = self.driver.find_element(*self.result_field)
        return result_element.text.strip()
    
    def wait_for_result(self, expected_result, delay_seconds):
        timeout = delay_seconds + 5
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            current_result = self.get_result()
            if current_result == expected_result:
                return True
            time.sleep(0.5)
        
        return False
    