from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        """
        Инициализация страницы авторизации

        Args:
            driver: WebDriver
        """
        self.driver = driver

    def open(self):
        """
        Открытие страницы авторизации

        Returns:
            None
        """
        self.driver.get("https://www.saucedemo.com/")

    def enter_username(self, username):
        """
        Ввод имени пользователя

        Args:
            username: str - имя пользователя

        Returns:
            None
        """
        self.driver.find_element(By.ID, "user-name").send_keys(username)

    def enter_password(self, password):
        """
        Ввод пароля

        Args:
            password: str - пароль

        Returns:
            None
        """
        self.driver.find_element(By.ID, "password").send_keys(password)

    def click_login_button(self):
        """
        Нажатие кнопки входа

        Returns:
            None
        """
        self.driver.find_element(By.ID, "login-button").click()

    def get_error_message(self):
        """
        Получение сообщения об ошибке

        Returns:
            str - текст сообщения об ошибке
        """
        selector = "[data-test='error']"
        return self.driver.find_element(By.CSS_SELECTOR, selector).text
