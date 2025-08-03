from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from CalculatorPage import CalculatorPage  # Импортируем класс


def test_slow_calculator():
    driver = webdriver.Chrome()  # Открываем браузер
    driver.maximize_window()  # Увеличиваем окно
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    calculator = CalculatorPage(driver)  # Переменная хранит экземпляр класса CalculatorPage

    # Подставляем значения в переменные
    calculator.set_delay(45)
    calculator.click_button("7")
    calculator.click_button("+")
    calculator.click_button("8")
    calculator.click_button("=")

    WebDriverWait(driver, 45).until(
        EC.text_to_be_present_in_element(calculator.result_screen, "15"))

    # Получаем результат, проверяем, закрываем браузер
    result = calculator.get_result()
    assert result == "15"
    driver.quit()
