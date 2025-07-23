from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# переход на сайт
driver.get("http://uitestingplayground.com/textinput")

# находим поле и вводим текст "SkyPro "
txt = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
txt.send_keys("SkyPro")

# ищем элемент с id="updatingButton" и кликаем
content = driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()
name = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
print(name.text)

driver.quit()
