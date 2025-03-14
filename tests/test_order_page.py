import pytest
from page_objects.main_page import MainPage
from page_objects.order_page import OrderPage
from data import TestData
import allure

class TestOrderPage:
    @allure.title("Успешное оформление заказа")
    @pytest.mark.parametrize("order_data, order_button_location",
                             [(data, "up") for data in TestData.ORDER_DATA_SETS] +
                             [(data, "down") for data in TestData.ORDER_DATA_SETS])
    def test_order_flow(self, driver, order_data, order_button_location):
        """Проверяет успешное оформление заказа с использованием разных кнопок."""
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        # 1. Нажатие кнопки "Заказать" (верхней или нижней)
        main_page.open()
        main_page.accept_cookies()
        main_page.click_order_button(order_button_location)  # Вызываем метод в MainPage

        # 2. Заполнение первой части формы
        order_page.enter_personal_data(order_data["firstname"], order_data["lastname"],
                                        order_data["address"], order_data["metro_station"],
                                        order_data["phone_number"])

        # 3. Нажатие кнопки "Далее"
        order_page.click_next_button()

        # 4. Заполнение второй части формы
        order_page.enter_rental_data(order_data["delivery_date"], order_data["rental_period"],
                                       order_data["color"], order_data["comment"])

        # 5. Нажатие кнопки "Заказать" на второй форме
        order_page.click_order_button()

        # 6. Подтверждение заказа во всплывающем окне
        order_page.confirm_order()

        # 7. Проверка отображения сообщения об успешном заказе
        assert order_page.is_order_success_displayed(), "Сообщение об успешном заказе не отображается"