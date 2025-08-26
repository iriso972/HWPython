import pytest
from selenium import webdriver
from LogPage import LogPage
from ShopPage import ShopPage
from CartPage import CartPage
from CheckoutPage import CheckoutPage


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_purchase(driver):
    # Создание страниц
    login_page = LogPage(driver)
    shop_page = ShopPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    # Открытие сайта и вход
    driver.get("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")

    # Добавление товаров
    items = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]
    for item in items:
        shop_page.add_item_to_cart(item)

    # Переход в корзину и оформление заказа
    shop_page.go_to_cart()
    cart_page.click_checkout()
    checkout_page.fill_info("Irina", "Bloshkina", "606123")

    # Проверка итоговой стоимости
    total = checkout_page.get_total()
    assert total == 58.29
