import allure
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from CalculatorPage import CalculatorPage


@allure.feature("Калькулятор с задержкой")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест калькулятора с 45-секундной задержкой")
@allure.description("""
Тест проверяет работу калькулятора с большой задержкой:
1. Устанавливаем задержку 45 секунд
2. Выполняем операцию 7 + 8
3. Ожидаем результат 15
4. Проверяем корректность вычислений
""")
def test_slow_calculator():
    with allure.step("Открываем браузер и инициализируем драйвер"):
        driver = webdriver.Chrome()
        driver.maximize_window()

    with allure.step("Переходим на страницу калькулятора"):
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    with allure.step("Создаем экземпляр страницы калькулятора"):
        calculator = CalculatorPage(driver)

    with allure.step("Настраиваем параметры калькулятора"):
        calculator.set_delay(45)

    with allure.step("Выполняем вычисление 7 + 8"):
        calculator.click_button("7")
        calculator.click_button("+")
        calculator.click_button("8")
        calculator.click_button("=")

    with allure.step("Ожидаем появления результата в течение 45 секунд"):
        WebDriverWait(driver, 46).until(
            EC.text_to_be_present_in_element(calculator.result_screen, "15")
        )

    with allure.step("Проверяем корректность результата"):
        result = calculator.get_result()
        assert result == "15", f"Ожидался результат '15', но получено '{result}'"
        allure.attach(f"Результат вычислений: {result}", name="Результат")

    with allure.step("Закрываем браузер"):
        driver.quit()