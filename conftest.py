import pytest
from selenium import webdriver
from .data import TestData
import allure

@pytest.fixture(scope='function')
def driver():
    with allure.step("Инициализация драйвера"):
        driver = webdriver.Firefox() #
        driver.get(TestData.SCOOTER_URL)

    yield driver

    with allure.step("Закрытие драйвера"):
        driver.quit()
