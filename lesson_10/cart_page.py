from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, driver):
        """
        Инициализация страницы корзины

        Args:
            driver: WebDriver
        """
        self.driver = driver

    def get_cart_items_count(self):
        """
        Получение количества товаров в корзине

        Returns:
            int - количество товаров
        """
        return len(self.driver.find_elements(By.CLASS_NAME, "cart_item"))

    def checkout(self):
        """
        Нажатие кнопки оформления заказа

        Returns:
            None
        """
        self.driver.find_element(By.ID, "checkout").click()
