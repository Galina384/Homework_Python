from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:

    def __init__(self, driver):
        """
        Инициализация страницы калькулятора

        Args:
            driver: WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def open(self):
        """
        Открытие страницы калькулятора

        Returns:
            None
        """
        url = (
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )
        self.driver.get(url)

    def set_delay(self, seconds):
        """
        Установка задержки

        Args:
            seconds: int - задержка в секундах

        Returns:
            None
        """
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(seconds)

    def click_button(self, button_text):
        """
        Нажатие кнопки

        Args:
            button_text: str - текст на кнопке

        Returns:
            None
        """
        xpath = f"//span[text()='{button_text}']"
        button = self.driver.find_element(By.XPATH, xpath)
        button.click()

    def get_result(self):
        """
        Получение результата

        Returns:
            str - текст результата
        """
        locator = (By.CSS_SELECTOR, ".screen")
        result_element = self.wait.until(
            EC.presence_of_element_located(locator)
        )
        return result_element.text

    def perform_calculation(self, expression):
        """
        Выполнение вычисления

        Args:
            expression: str - строка с выражением

        Returns:
            None
        """
        for char in expression:
            self.click_button(char)
