from time import sleep

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/login")

username_input = driver.find_element(By.ID,"username")
username_input.send_keys('tomsmith')

password_input = driver.find_element(By.ID,"password")
password_input.send_keys("SuperSecretPassword!")
sleep(5)

login_button = driver.find_elements(By.ID, "button")
login_button.click()

flash_message = driver.find_element(By.CSS_SELECTOR, "div.flash.success")
print(flash_message.text)
driver.quit()