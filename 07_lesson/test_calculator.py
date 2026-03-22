import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from calculator_page import CalculatorPage

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    
    driver = webdriver.Chrome(options=chrome_options)
    
    yield driver
    
    driver.quit()
def test_calculator_addition_with_delay(driver):
    calculator = CalculatorPage(driver)
    
    calculator.open("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    calculator.set_delay(45)
    
    calculator.click_sequence(["7", "+", "8", "="])
    
    result_found = calculator.wait_for_result("15", 45)
    
    assert result_found == True, "Результат 15 не появился!"