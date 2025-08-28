from selenium.webdriver.common.by import By
import allure


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Нажать кнопку оформления заказа")
    def click_checkout(self) -> None:
        self.driver.find_element(By.ID, "checkout").click()
