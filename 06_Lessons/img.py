from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
)

WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element((By.ID, "text"), "Done!")
)

images = driver.find_elements(By.TAG_NAME, "img")
src = images[2].get_attribute("src")
print(src)

driver.quit()
