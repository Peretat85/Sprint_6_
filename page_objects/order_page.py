from .base_page import BasePage
from locators import OrderPageLocators
from data import TestData
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = TestData.SCOOTER_URL_ORDER # переход к странице заказа

    def open(self):
        self.open_page(self.url)  # Используем метод open_page из BasePage

    def enter_personal_data(self, firstname, lastname, address, metro_station, phone_number):
        """Вводит персональные данные на первой странице формы."""
        self.send_keys(OrderPageLocators.FIRSTNAME_INPUT, firstname)
        self.send_keys(OrderPageLocators.LASTNAME_INPUT, lastname)
        self.send_keys(OrderPageLocators.ADDRESS_INPUT, address)
        self.select_metro_station(metro_station)  # Используем отдельный метод для выбора станции
        self.send_keys(OrderPageLocators.PHONE_NUMBER_INPUT, phone_number)

    def select_metro_station(self, station_name):
        """Выбирает станцию метро из выпадающего списка."""
        metro_station_input = self.driver.find_element(*OrderPageLocators.METRO_STATION_INPUT)
        metro_station_input.send_keys(station_name)
        time.sleep(0.5)  # Даем время на появление списка (очень важно!)

        # Нажимаем клавишу "Вниз"
        metro_station_input.send_keys(Keys.DOWN)
        time.sleep(0.2)  # Небольшая задержка между нажатиями

        metro_station_input.send_keys(Keys.ENTER)  # Выбираем станцию

    def click_next_button(self):
        """Нажимает кнопку 'Далее'."""
        self.click(OrderPageLocators.NEXT_BUTTON)

    def enter_rental_data(self, delivery_date, rental_period, comment):
        """Вводит данные об аренде на второй странице формы."""
        # дата доставки
        date_delivery = self.driver.find_element(*OrderPageLocators.DELIVERY_DATE_INPUT)
        date_delivery.send_keys(delivery_date)
      #  self.send_keys(OrderPageLocators.DELIVERY_DATE_INPUT, delivery_date)
        date_delivery.send_keys(Keys.ENTER)

        # Выбираем срок аренды
        self.click(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        rental_period_locator = (By.XPATH, OrderPageLocators.RENTAL_PERIOD_VALUE[1].format(period=rental_period))
        self.click(rental_period_locator)

        # Выбираем цвет * необязательный параметр - пропустить
        # color_locator = (By.XPATH, OrderPageLocators.COLOR_CHECKBOX[1].format(color=color))
        # self.click(color_locator)

        self.send_keys(OrderPageLocators.COMMENT_INPUT, comment)

    def click_order_button(self):
        """Нажимает финальную кнопку 'Заказать'."""
        self.click(OrderPageLocators.ORDER_BUTTON_FINAL)

    def confirm_order(self):
        """Подтверждает заказ во всплывающем окне."""
        self.click(OrderPageLocators.CONFIRMATION_MODAL_BUTTON)

    def is_order_success_displayed(self):
        """Проверяет, отображается ли сообщение об успешном заказе."""
        return self.is_element_displayed(OrderPageLocators.ORDER_SUCCESS_MODAL)

