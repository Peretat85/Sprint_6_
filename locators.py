from selenium.webdriver.common.by import By

class MainPageLocators:
    ORDER_BUTTON_UP = (By.CLASS_NAME, "Button_Button__ra12g") # Верхняя кнопка.
    ORDER_BUTTON_DOWN = (By.XPATH, "//div[@class='Home_FinishButton__1_cWm']/button") # Нижняя кнопка.
    SAMOKAT_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    COOKIES_BUTTON = (By.ID, "rcc-confirm-button") # Кнопка "да все привыкли" (cookie)

    # Локаторы для вопросов FAQ
    FAQ_QUESTIONS = [
        (By.ID, 'accordion__heading-0'), (By.ID, 'accordion__heading-1'), (By.ID, 'accordion__heading-2'),
        (By.ID, 'accordion__heading-3'), (By.ID, 'accordion__heading-4'), (By.ID, 'accordion__heading-5'),
        (By.ID, 'accordion__heading-6'), (By.ID, 'accordion__heading-7')
    ]
    FAQ_ANSWERS = [
        (By.ID, 'accordion__panel-0'), (By.ID, 'accordion__panel-1'), (By.ID, 'accordion__panel-2'),
        (By.ID, 'accordion__panel-3'), (By.ID, 'accordion__panel-4'), (By.ID, 'accordion__panel-5'),
        (By.ID, 'accordion__panel-6'), (By.ID, 'accordion__panel-7')
    ]

class OrderPageLocators:
    FIRSTNAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LASTNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_INPUT = (By.CLASS_NAME, "select-search__input")
    PHONE_NUMBER_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    DELIVERY_DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")
    RENTAL_PERIOD_VALUE = (By.XPATH, "//div[contains(@class, 'Dropdown-menu')]//div[text()='{period}']")  # {period} заменить на значение
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']") #
    ORDER_BUTTON_FINAL = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and contains(text(), 'Заказать')]")
    CONFIRMATION_MODAL_BUTTON = (By.XPATH, "//button[text()='Да']")
    ORDER_SUCCESS_MODAL = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]")