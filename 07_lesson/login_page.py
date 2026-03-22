from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
    
    def open(self, url):
        """Открыть страницу"""
        self.driver.get(url)
    
    def enter_username(self, username):
        """Ввести логин"""
        field = self.driver.find_element(*self.username_input)
        field.clear()
        field.send_keys(username)
    
    def enter_password(self, password):
        """Ввести пароль"""
        field = self.driver.find_element(*self.password_input)
        field.clear()
        field.send_keys(password)
    
    def click_login(self):
        """Нажать кнопку входа"""
        button = self.driver.find_element(*self.login_button)
        button.click()
    
    def login(self, username, password):
        """Выполнить вход (всё вместе)"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()