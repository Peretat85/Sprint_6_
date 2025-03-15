from .base_page import BasePage
from locators import MainPageLocators
from data import TestData
from allure import step

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
       # self.url = TestData.SCOOTER_URL

    @step("Открыть главную страницу")
    def open(self):
        self.open_page(self.url)

    @step("Кликнуть кнопку 'Заказать' ({button_location})")
    def click_order_button(self, button_location="up"):
        """Нажимает кнопку 'Заказать' (вверху или внизу страницы)."""
        if button_location == "up":
            self.click(MainPageLocators.ORDER_BUTTON_UP)
        elif button_location == "down":
            self.click(MainPageLocators.ORDER_BUTTON_DOWN)
        else:
            raise ValueError("Invalid button location. Must be 'up' or 'down'.")


    @step("Кликнуть на логотип 'Самокат'")
    def click_samokat_logo(self):
        """Нажимает на логотип 'Самоката'."""
        self.click(MainPageLocators.SAMOKAT_LOGO)


    @step("Кликнуть на логотип 'Яндекса'")
    def click_yandex_logo(self):
        """Нажимает на логотип 'Яндекса'."""
        self.click(MainPageLocators.YANDEX_LOGO)

    @step("Принять cookies")
    def accept_cookies(self):
        """Принимает cookies (если есть)."""
        if self.is_element_displayed(MainPageLocators.COOKIES_BUTTON, timeout=2):  # Проверяем, что кнопка вообще есть
            self.click(MainPageLocators.COOKIES_BUTTON)


    @step("Получить текст ответа на вопрос FAQ {question_index}")
    def get_faq_answer(self, question_index):
        """Кликает на вопрос FAQ и возвращает текст ответа."""
        question_locator = MainPageLocators.FAQ_QUESTIONS[question_index]
        answer_locator = MainPageLocators.FAQ_ANSWERS[question_index]

        self.click(question_locator)

        self.wait_for_element_visibility(answer_locator)
        return self.get_element_text(answer_locator)

    @step("Получить текущий URL страницы")
    def get_current_url(self):
        """Возвращает текущий URL страницы."""
        return self.driver.current_url

    @step("Переключиться на последнее открытое окно")
    def switch_to_last_window(self):
        """Переключается на последнее открытое окно."""
        original_window = self.driver.current_window_handle
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                return  # Выходим после переключения, предполагая, что переключились успешно
        raise Exception("Не найдено новое окно для переключения.")  # Если не найдено, вызываем исключение

    @step("Ожидать количество окон: {num_windows}")
    def wait_for_number_of_windows(self, num_windows, timeout=10):
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.support.ui import WebDriverWait
        WebDriverWait(self.driver, timeout).until(EC.number_of_windows_to_be(num_windows))

    @step("Ожидать, что URL содержит: {url_part}")
    def wait_for_url_contains(self, url_part, timeout=10):
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.support.ui import WebDriverWait
        WebDriverWait(self.driver, timeout).until(EC.url_contains(url_part))