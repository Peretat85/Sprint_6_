import pytest
from page_objects.main_page import MainPage
from page_objects.order_page import OrderPage
from data import TestData
from locators import MainPageLocators
import allure #Импорт allure


class TestOrderPage:
    @pytest.mark.parametrize("order_button_locator", [MainPageLocators.ORDER_BUTTON_UP, MainPageLocators.ORDER_BUTTON_DOWN])
    @pytest.mark.parametrize("order_data", TestData.ORDER_DATA_SETS)
    @allure.title("Оформление заказа")
    def test_order_scooter(self, driver, order_button_locator, order_data):
        """Проверяет оформление заказа самоката с разными точками входа и данными."""
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open()
        main_page.accept_cookies()
        main_page.click_order_button(
            button_location="up" if order_button_locator == MainPageLocators.ORDER_BUTTON_UP else "down"
        )  # Определяем, какая кнопка нажата

        # Заполняем первую страницу
        order_page.enter_personal_data(
            firstname=order_data["firstname"],
            lastname=order_data["lastname"],
            address=order_data["address"],
            metro_station=order_data["metro_station"],
            phone_number=order_data["phone_number"]
        )
        order_page.click_next_button()

        # Заполняем вторую страницу
        order_page.enter_rental_data(
            delivery_date=order_data["delivery_date"],
            rental_period=order_data["rental_period"],
          #  color=order_data["color"],
            comment=order_data["comment"]
        )
        order_page.click_order_button()
        order_page.confirm_order()

        # Проверяем успешное создание заказа
        assert order_page.is_order_success_displayed(), "Сообщение об успешном заказе не отображается."