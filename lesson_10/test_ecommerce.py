import allure
import pytest
from selenium import webdriver
from login_page import LoginPage
from products_page import ProductsPage


@allure.feature("Интернет-магазин")
class TestEcommerce:

    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome()
        yield driver
        driver.quit()

    @allure.title("Успешная авторизация")
    @allure.description("Тест проверяет вход с валидными данными")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_successful_login(self, driver):
        with allure.step("Открыть страницу авторизации"):
            login_page = LoginPage(driver)
            login_page.open()

        with allure.step("Ввести имя пользователя"):
            login_page.enter_username("standard_user")

        with allure.step("Ввести пароль"):
            login_page.enter_password("secret_sauce")

        with allure.step("Нажать кнопку входа"):
            login_page.click_login_button()

        with allure.step("Проверка результата"):
            products_page = ProductsPage(driver)
            assert products_page.get_page_title() == "Products"
