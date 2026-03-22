import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from login_page import LoginPage
from products_page import ProductsPage
from cart_page import CartPage
from checkout_page import CheckoutPage

@pytest.fixture
def driver():

    firefox_options = Options()
    firefox_options.add_argument("--start-maximized")

    driver = webdriver.Firefox(options=firefox_options)
    
    yield driver


    driver.quit()

def test_checkout_total(driver):

    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open("https://www.saucedemo.com/")

    login_page.login("standard_user", "secret_sauce")

    products_to_add = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]
    products_page.add_products_to_cart(products_to_add)

    products_page.go_to_cart()


    cart_page.click_checkout()

    checkout_page.fill_form(
        first_name="Иван",
        last_name="Петров",
        postal_code="123456"
    )
    checkout_page.click_continue()

    total = checkout_page.get_total()

    assert total == "$58.29", f"Ожидалось $58.29, а получилось {total}"

    print(f"\n✅ Тест пройден! Итоговая сумма: {total}")