from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/inputs")
sleep(2)

input_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")

input_field.send_keys("12345")
sleep(1)

input_field.clear()
sleep(1)

input_field.send_keys("54321")
sleep(2)

driver.quit()
