from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_ajax_button():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        driver.get("http://uitestingplayground.com/ajax")

        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "ajaxButton"))
        )
        button.click()

        success_text = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-success"))
        ).text

        print(success_text)

    finally:
        driver.quit()


if __name__ == "__main__":
    test_ajax_button()
