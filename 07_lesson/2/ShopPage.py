from selenium.webdriver.common.by import By


class ShopPage:
    def __init__(self, driver):
        self.driver = driver

    def add_item_to_cart(self, item_name):
        button_locator = (By.XPATH, f"//div[@class='inventory_item' and .//div[contains(text(), '{item_name}')]]//button")
        self.driver.find_element(*button_locator).click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
