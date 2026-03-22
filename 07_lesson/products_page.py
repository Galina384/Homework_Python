from selenium.webdriver.common.by import By

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        # Корзина
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")
        # Счетчик в корзине
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
    
    def add_product_to_cart(self, product_name):
        """
        Добавить товар в корзину по названию
        """

        add_button = self.driver.find_element(
            By.XPATH, 
            f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button[contains(@id, 'add-to-cart')]"
        )
        add_button.click()
    
    def add_products_to_cart(self, product_names):
        """Добавить несколько товаров"""
        for name in product_names:
            self.add_product_to_cart(name)
    
    def go_to_cart(self):
        """Перейти в корзину"""
        cart = self.driver.find_element(*self.cart_icon)
        cart.click()
    
    def get_cart_count(self):
        """Узнать, сколько товаров в корзине"""
        try:
            badge = self.driver.find_element(*self.cart_badge)
            return int(badge.text)
        except:
            return 0