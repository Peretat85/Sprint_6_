import pytest
from page_objects.main_page import MainPage
from page_objects.order_page import OrderPage
from data import TestData
#from locators import MainPageLocators
import allure #Импорт allure

class TestMainPage:
    @allure.title('Проверка перехода на главную по лого Самокат')  # декораторы
    def test_samokat_logo_navigation(self, driver):
        """Проверяет переход на главную страницу по клику на логотип 'Самоката'."""
        main_page = MainPage(driver)
        main_page.open()  # Открываем главную
        order_page = OrderPage(driver)
        order_page.open() # Открываем страницу заказа

        main_page.click_samokat_logo()

        current_url = main_page.get_current_url()
        assert current_url == TestData.SCOOTER_URL, "Не удалось перейти на главную страницу Самоката"

    @allure.title('Проверка перехода в Дзен по лого Яндекс')
    def test_yandex_logo_navigation(self, driver):
        #"""Проверяет переход на страницу Дзена по клику на логотип 'Яндекса'."""
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_yandex_logo()

        # Ожидаем открытия нового окна
        main_page.wait_for_number_of_windows(2)

        # Переключаемся на новое окно
        main_page.switch_to_last_window()

        # Проверяем, что открылась страница Дзена
        main_page.wait_for_url_contains(TestData.DZEN_URL)
        current_url = main_page.get_current_url()
        assert TestData.DZEN_URL in current_url, "Не удалось перейти на страницу Дзена"

    @allure.title('Проверка списка FAQ')
    @pytest.mark.parametrize("question_index", range(len(TestData.FAQ_DATA)))
    def test_faq_answers(self, driver, question_index):
        """Проверяет, что текст ответа на вопрос FAQ соответствует ожидаемому"""
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()

        # Извлекаем ожидаемый ответ из данных для вопроса
        expected_answer = TestData.FAQ_DATA[question_index]['expected_answer']

        actual_answer = main_page.get_faq_answer(question_index)

        assert actual_answer == expected_answer, f"Неверный текст ответа для вопроса {question_index}"


