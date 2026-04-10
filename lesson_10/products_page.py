from selenium.webdriver.common.by import By


class ProductsPage:

    def __init__(self, driver):
        """
        Инициализация страницы товаров

        Args:
            driver: WebDriver
        """
        self.driver = driver

    def get_page_title(self):
        """
        Получение заголовка страницы

        Returns:
            str - текст заголовка
        """
        return self.driver.find_element(By.CSS_SELECTOR, ".title").text

    def add_product_to_cart(self, product_name):
        """
        Добавление товара в корзину

        Args:
            product_name: str - название товара

        Returns:
            None
        """
        product_id = product_name.lower().replace(" ", "-")
        self.driver.find_element(By.ID, f"add-to-cart-{product_id}").click()

    def go_to_cart(self):
        """
        Переход в корзину

        Returns:
            None
        """
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
