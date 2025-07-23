from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# переход на сайт
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# загрузка картинок, ожидание
waiter =WebDriverWait(driver, 17)
waiter.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#landscape")))

# получаем картинки
images = driver.find_element(By.CSS_SELECTOR, "#award")

# находим 3 элемент и выводим на печать src
medal_src = images.get_attribute("src")
print(medal_src)

driver.quit()
