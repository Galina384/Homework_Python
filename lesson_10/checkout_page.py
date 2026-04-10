from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        """
        Инициализация страницы оформления заказа

        Args:
            driver: WebDriver
        """
        self.driver = driver

    def fill_checkout_info(self, first_name, last_name, postal_code):
        """
        Заполнение информации о покупателе

        Args:
            first_name: str - имя
            last_name: str - фамилия
            postal_code: str - почтовый индекс

        Returns:
            None
        """
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)

    def click_continue(self):
        """
        Нажатие кнопки продолжения

        Returns:
            None
        """
        self.driver.find_element(By.ID, "continue").click()

    def get_total_amount(self):
        """
        Получение итоговой суммы

        Returns:
            str - итоговая сумма
        """
        element = self.driver.find_element(
            By.CLASS_NAME, "summary_total_label")
        return element.text

    def click_finish(self):
        """
        Нажатие кнопки завершения заказа

        Returns:
            None
        """
        self.driver.find_element(By.ID, "finish").click()

    def get_complete_message(self):
        """
        Получение сообщения о завершении заказа

        Returns:
            str - текст сообщения
        """
        return self.driver.find_element(By.CLASS_NAME, "complete-header").text
