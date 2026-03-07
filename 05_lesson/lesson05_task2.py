from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid")
sleep(2)

driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()

sleep(1)
driver.quit()
