from selenium.webdriver.common.by import By
import allure


class LogPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Авторизация пользователя '{username}'")
    def login(self, username: str, password: str) -> None:
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
