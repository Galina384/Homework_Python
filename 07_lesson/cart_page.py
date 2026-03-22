from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")
        self.continue_shopping_button = (By.ID, "continue-shopping")
        self.cart_items = (By.CLASS_NAME, "cart_item")
    
    def click_checkout(self):
        """Нажать кнопку Checkout"""
        button = self.driver.find_element(*self.checkout_button)
        button.click()
    
    def get_cart_items_count(self):
        """Сколько товаров в корзине"""
        items = self.driver.find_elements(*self.cart_items)
        return len(items)
    
    def get_cart_item_names(self):
        """Получить названия всех товаров в корзине"""
        items = self.driver.find_elements(*self.cart_items)
        names = []
        for item in items:
            name_element = item.find_element(By.CLASS_NAME, "inventory_item_name")
            names.append(name_element.text)
        return names