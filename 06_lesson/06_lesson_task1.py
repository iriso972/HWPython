from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# поместим метод перед переходом на сайт
driver.implicitly_wait(17)
driver.get("http://www.uitestingplayground.com/ajax")

# нажимаем на кнопку
driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

# ищем элемент с id="content"
content = driver.find_element(By.CSS_SELECTOR, "#content")

# собираем текст из элемента с тегом p и class="bg-success"
# через элемент в content
txt = content.find_element(By.CSS_SELECTOR, "p.bg-success").text
print(txt)

driver.quit()
