import pytest
import allure
from selenium import webdriver
from LogPage import LogPage
from ShopPage import ShopPage
from CartPage import CartPage
from CheckoutPage import CheckoutPage


@pytest.fixture()
def driver():
    with allure.step("Инициализация драйвера браузера"):
     driver = webdriver.Firefox()
     driver.maximize_window()
     yield driver
     driver.quit()

@allure.title("Тест оформления покупки в интернет-магазине")
@allure.description("Проверка полного цикла покупки: авторизация, добавление товаров, оформление заказа")
@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
def test_purchase(driver):
    # Создание страниц
    login_page = LogPage(driver)
    shop_page = ShopPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    with allure.step("Открытие сайта и авторизация"):

        driver.get("https://www.saucedemo.com/")
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Добавление товаров в корзину"):
        items = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]
        for item in items:
            shop_page.add_item_to_cart(item)

    with allure.step("Переход в корзину и оформление заказа"):
        shop_page.go_to_cart()
        cart_page.click_checkout()
        checkout_page.fill_info("Irina", "Bloshkina", "606123")

    with allure.step("Проверка итоговой стоимости"):
        total = checkout_page.get_total()
        assert total == 58.29, f"Ожидаемая сумма: 58.29, Фактическая: {total}"
