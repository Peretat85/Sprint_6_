from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait_for_element_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def click(self, locator):
        element = self.wait_for_element_clickable(locator)
        element.click()

    def send_keys(self, locator, text):
        element = self.wait_for_element(locator)
        element.send_keys(text)

    def get_element_text(self, locator):
        element = self.wait_for_element(locator)
        return element.text

    def is_element_displayed(self, locator, timeout=5):
        """Проверяет, отображается ли элемент на странице."""
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False