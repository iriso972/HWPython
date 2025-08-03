from selenium.webdriver.common.by import By
class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_screen = (By.CSS_SELECTOR, ".screen")
        self.buttons = {
            "7": (By.XPATH, '//span[text()="7"]'),
            "+": (By.XPATH, '//span[text()="+"]'),
            "8": (By.XPATH, '//span[text()="8"]'),
            "=": (By.XPATH, '//span[text()="="]')
        }

    def set_delay(self, seconds):
        element = self.driver.find_element(*self.delay_input)
        element.clear()
        element.send_keys(str(seconds))

    def click_button(self, symbol):
        button = self.driver.find_element(*self.buttons[symbol])
        button.click()

    def get_result(self):
        return self.driver.find_element(*self.result_screen).text
