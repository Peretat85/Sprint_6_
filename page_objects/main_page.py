from .base_page import BasePage
from locators import MainPageLocators
from data import TestData
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = TestData.SCOOTER_URL

    def open(self):
        self.open_page(self.url)

    def click_order_button(self, button_location="up"):
        """Нажимает кнопку 'Заказать' (вверху или внизу страницы)."""
        if button_location == "up":
            self.click(MainPageLocators.ORDER_BUTTON_UP)
        elif button_location == "down":
            self.click(MainPageLocators.ORDER_BUTTON_DOWN)
        else:
            raise ValueError("Invalid button location. Must be 'up' or 'down'.")

    def click_samokat_logo(self):
        """Нажимает на логотип 'Самоката'."""
        self.click(MainPageLocators.SAMOKAT_LOGO)

    def click_yandex_logo(self):
        """Нажимает на логотип 'Яндекса'."""
        self.click(MainPageLocators.YANDEX_LOGO)

    def accept_cookies(self):
        """Принимает cookies (если есть)."""
        if self.is_element_displayed(MainPageLocators.COOKIES_BUTTON, timeout=2): #Проверяем, что кнопка вообще есть
           self.click(MainPageLocators.COOKIES_BUTTON)

    def get_faq_answer(self, question_index):
        """Кликает на вопрос FAQ и возвращает текст ответа."""
        question_locator = MainPageLocators.FAQ_QUESTIONS[question_index]
        answer_locator = MainPageLocators.FAQ_ANSWERS[question_index]

        # ждем видимости и кликабельности элементов
        element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(question_locator)
        )

        element = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(question_locator)
        )

        # Прокрутка элемента в центр окна с помощью JavaScript
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(0.5)
        element.click()

        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(answer_locator))
        return self.get_element_text(answer_locator)