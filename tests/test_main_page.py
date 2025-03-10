import pytest
from page_objects.main_page import MainPage
from page_objects.order_page import OrderPage
from data import TestData
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import allure #Импорт allure

class TestMainPage:
    @allure.title('Проверка перехода на главную по лого Самокат')  # декораторы
    def test_samokat_logo_navigation(self, driver):
        #"""Проверяет переход на главную страницу по клику на логотип 'Самоката'."""
        main_page = MainPage(driver)
        main_page.open() # Открываем главную
        order_page = OrderPage(driver)
        order_page.open() # переход на страницу заказа
        main_page.click_samokat_logo()
        assert driver.current_url == TestData.SCOOTER_URL, "Не удалось перейти на главную страницу Самоката"

    @allure.title('Проверка перехода в Дзен по лого Яндекс')
    def test_yandex_logo_navigation(self, driver):
        #"""Проверяет переход на страницу Дзена по клику на логотип 'Яндекса'."""
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_yandex_logo()

        # Ожидаем открытия нового окна
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

        # Переключаемся на новое окно
        original_window = driver.current_window_handle
        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break

        # Проверяем, что открылась страница Дзена
        WebDriverWait(driver, 10).until(EC.url_contains(TestData.DZEN_URL))
        assert TestData.DZEN_URL in driver.current_url, "Не удалось перейти на страницу Дзена"

        # Закрываем новое окно и переключаемся обратно на исходное
        driver.close()
        driver.switch_to.window(original_window)


    @pytest.mark.parametrize("faq_data", TestData.FAQ_DATA)
    @allure.title('Проверка списка FAQ')
    def test_faq_dropdown(self, driver, faq_data):
        #"""Проверяет открытие выпадающего списка и отображение текста для каждого вопроса FAQ."""
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()
        expected_answer = faq_data["expected_answer"]
        actual_answer = main_page.get_faq_answer(faq_data["question_index"])
        assert actual_answer == expected_answer, f"Неверный текст ответа для вопроса {faq_data['question_index']}"

