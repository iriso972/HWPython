from selenium.webdriver.common.by import By
import allure


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Заполнение информации для оформления: {first_name} {last_name}, {postal_code}")
    def fill_info(self, first_name: str, last_name: str, postal_code: str) -> None:
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()

    @allure.step("Получить итоговую сумму заказа")
    def get_total(self) -> float:
        total_text = self.driver.find_element(By.CLASS_NAME, "summary_total_label").text
        return float(total_text.split("$")[1])
