from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# объявляем функцию
def test_slow_calculator():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

# выставляем время задержки
    pole = driver.find_element(By.CSS_SELECTOR, "#delay")
    pole.clear()
    pole.send_keys("45")

    driver.find_element(By.XPATH, '//span[text()="7"]').click()
    driver.find_element(By.XPATH, '//span[text()="+"]').click()
    driver.find_element(By.XPATH, '//span[text()="8"]').click()
    driver.find_element(By.XPATH, '//span[text()="="]').click()
    WebDriverWait(driver, 48).until(EC.text_to_be_present_in_element
                                        ((By.CSS_SELECTOR, ".screen"), "15"))
    res = driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert res == "15"

    driver.quit()
