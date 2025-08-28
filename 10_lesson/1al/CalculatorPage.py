from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.remote.webelement import WebElement
from typing import Dict, Tuple


class CalculatorPage:
    def __init__(self, driver):
        """
        Конструктор класса CalculatorPage.

        :param driver: WebDriver - объект драйвера Selenium для управления браузером
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_screen = (By.CSS_SELECTOR, ".screen")
        self.buttons = {
            "7": (By.XPATH, '//span[text()="7"]'),
            "+": (By.XPATH, '//span[text()="+"]'),
            "8": (By.XPATH, '//span[text()="8"]'),
            "=": (By.XPATH, '//span[text()="="]')
        }

    @allure.step("Выставляем задержку {seconds} секунд")
    def set_delay(self, seconds: int) -> None:
        """
        Устанавливает задержку для выполнения операций на калькуляторе.

        :param seconds: Количество секунд задержки
        :type seconds: int
        :return: None
        """
        element = self.driver.find_element(*self.delay_input)
        element.clear()
        element.send_keys(str(seconds))

    @allure.step("Нажимаем кнопку '{symbol}'")
    def click_button(self, symbol: str) -> None:
        """
        Нажимает указанную кнопку на калькуляторе.

        :param symbol: Символ кнопки для нажатия (например: "7", "+", "8", "=")
        :type symbol: str
        :return: None
        """
        button = self.driver.find_element(*self.buttons[symbol])
        button.click()

    @allure.step("Получаем результат вычислений")
    def get_result(self) -> str:
        """
        Получает текстовое значение с экрана калькулятора.

        :return: Текст результата вычислений
        :rtype: str
        """
        return self.driver.find_element(*self.result_screen).text