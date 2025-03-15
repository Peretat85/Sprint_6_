# page_objects/order_page.py
from .base_page import BasePage
from locators import OrderPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys  # Импортируем Keys
from allure import step
from data import TestData

class OrderPage(BasePage):

    @step("Открыть страницу заказа")
    def open(self):
        self.open_page(TestData.SCOOTER_URL_ORDER)

    @step("Ввести персональные данные: имя={firstname}, фамилия={lastname}, адрес={address}, метро={metro_station}, телефон={phone_number}")
    def enter_personal_data(self, firstname, lastname, address, metro_station, phone_number):
        """Заполняет первую страницу формы заказа."""
        self.send_keys(OrderPageLocators.FIRSTNAME_INPUT, firstname)
        self.send_keys(OrderPageLocators.LASTNAME_INPUT, lastname)
        self.send_keys(OrderPageLocators.ADDRESS_INPUT, address)
        self.select_metro_station(metro_station)
        self.send_keys(OrderPageLocators.PHONE_NUMBER_INPUT, phone_number)

    @step("Выбрать станцию метро: {metro_station}")
    def select_metro_station(self, metro_station):
        """Выбирает станцию метро из выпадающего списка (кликом или Enter)."""
        """Выбирает станцию метро из выпадающего списка."""
        metro_station_input = self.driver.find_element(*OrderPageLocators.METRO_STATION_INPUT)
        metro_station_input.send_keys(metro_station)

        # Нажимаем клавишу "Вниз"
        metro_station_input.send_keys(Keys.DOWN)

        metro_station_input.send_keys(Keys.ENTER)  # Выбираем станцию

    @step("Нажать кнопку 'Далее'")
    def click_next_button(self):
        """Нажимает кнопку 'Далее'."""
        self.click(OrderPageLocators.NEXT_BUTTON)

    @step("Ввести данные об аренде: дата доставки={delivery_date}, срок аренды={rental_period}, комментарий={comment}")
    def enter_rental_data(self, delivery_date, rental_period, color, comment): #Добавили color, чтобы не было ошибок
        """Заполняет вторую страницу формы заказа."""
        self.send_keys(OrderPageLocators.DELIVERY_DATE_INPUT, delivery_date)
        date = self.find_element(OrderPageLocators.DELIVERY_DATE_INPUT)
        date.send_keys(Keys.ENTER)
        self.select_rental_period(rental_period)
        #self.select_scooter_color(color) #TODO: Добавить выбор цвета, если есть
        self.send_keys(OrderPageLocators.COMMENT_INPUT, comment)

    @step("Выбрать срок аренды: {rental_period}")
    def select_rental_period(self, rental_period):
        """Выбирает срок аренды из выпадающего списка."""
        self.click(OrderPageLocators.RENTAL_PERIOD_DROPDOWN) #Открываем дропдаун
        rental_period_locator = (By.XPATH, f"//div[contains(@class, 'Dropdown-menu')]//div[text()='{rental_period}']")
        self.click(rental_period_locator)

    @step("Нажать финальную кнопку 'Заказать'")
    def click_order_button(self):
        """Нажимает финальную кнопку 'Заказать'."""
        self.click(OrderPageLocators.ORDER_BUTTON_FINAL)

    @step("Подтвердить заказ")
    def confirm_order(self):
        """Подтверждает заказ в модальном окне."""
        self.click(OrderPageLocators.CONFIRMATION_MODAL_BUTTON)

    @step("Проверить, что отображается сообщение об успешном заказе")
    def is_order_success_displayed(self, timeout=10):
        """Проверяет, что отображается модальное окно с сообщением об успешном заказе."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(OrderPageLocators.ORDER_SUCCESS_MODAL)
            )
            return True
        except:
            return False

    @step("Ввести текст {text} в элемент с локатором {locator}")
    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)

    @step("Найти элемент с локатором {locator}")
    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
    @step("Кликнуть на элемент по локатору {locator}")
    def click(self, locator, timeout=10):
        element = self.find_element(locator,timeout)
        try:
            element.click()
        except Exception as e:
            print(f"Ошибка при клике: {e}. Попытка клика через JavaScript.")
            self.execute_script("arguments[0].click();", element)

    @step("Выполнить JavaScript: {script}")
    def execute_script(self, script, element=None):
         """Выполняет JavaScript код."""
         if element:
              self.driver.execute_script(script, element)
         else:
              self.driver.execute_script(script)