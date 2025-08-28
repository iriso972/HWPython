from selenium.webdriver.common.by import By
import allure


class ShopPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Добавить товар '{item_name}' в корзину")
    def add_item_to_cart(self, item_name: str) -> None:
        button_locator = (By.XPATH, f"//div[@class='inventory_item' and .//div[contains(text(), '{item_name}')]]//button")
        self.driver.find_element(*button_locator).click()

    @allure.step("Перейти в корзину покупок")
    def go_to_cart(self) -> None:
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()