from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.remote.webdriver import WebDriver
#from selenium.webdriver.common.by import By
from allure import step
from data import TestData

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = TestData.SCOOTER_URL

    @step("Открыть страницу {url}")
    def open_page(self, url):
        self.driver.get(url)

    @step("Найти один элемент по локатору {locator}")
    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    @step("Найти несколько элементов по локатору {locator}")
    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator))

    @step("Дождаться кликабельности элемента по локатору {locator}") #*
    def wait_for_element_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
       )

    @step("Ожидать видимость элемента по локатору {locator}")
    def wait_for_element_visibility(self, locator, timeout=10):
        """Ожидает, пока элемент станет видимым."""
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @step("Кликнуть на элемент по локатору {locator}")
    def click(self, locator, timeout=10):
        element = self.find_element(locator,timeout)
        #element = self.wait_for_element_clickable(locator, timeout)
        #element.click()
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

    @step("Ввести текст '{text}' в элемент по локатору {locator}")
    def send_keys(self, locator, text, timeout=10):
        # Вводит текст в элемент
        element = self.find_element(locator, timeout)
        element.send_keys(text)

    @step("Получить текст элемента по локатору {locator}")
    def get_element_text(self, locator, timeout=10):
        #Получает текст элемента
        element = self.find_element(locator, timeout)
        return element.text

    @step("Проверка отображения элемента по локатору {locator}")
    def is_element_displayed(self, locator, timeout=10):
        """Проверяет, отображается ли элемент на странице."""
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False