import pytest
from selenium import webdriver
from .data import TestData

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    driver.get(TestData.SCOOTER_URL)

    yield driver

    driver.quit()

