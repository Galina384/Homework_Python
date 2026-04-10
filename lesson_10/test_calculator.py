import allure
import pytest
from selenium import webdriver
from calculator_page import CalculatorPage


@allure.feature("Калькулятор")
class TestCalculator:

    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome()
        yield driver
        driver.quit()

    @allure.title("Проверка сложения с задержкой")
    @allure.description("Проверка сложения 1+2=3 с задержкой 45 сек")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_addition_with_delay(self, driver):
        with allure.step("Открыть страницу калькулятора"):
            calc_page = CalculatorPage(driver)
            calc_page.open()

        with allure.step("Установить задержку 45 секунд"):
            calc_page.set_delay(45)

        with allure.step("Выполнить вычисление 1+2="):
            calc_page.perform_calculation("1+2=")

        with allure.step("Проверить результат"):
            assert calc_page.get_result() == "3"
