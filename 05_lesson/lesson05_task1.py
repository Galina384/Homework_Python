from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/classattr")
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
time.sleep(1)
driver.switch_to.alert.accept()

driver.quit()
