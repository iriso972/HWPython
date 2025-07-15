from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/classattr")
driver.find_element(By.XPATH,"//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]").click()
sleep(10)