import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    @allure.step('Ждём видимости элемента')
    def wait_for_element(self, locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Ждём пока элемент станет невидимым')
    def wait_for_element_hide(self, locator, timeout=30):
        WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Перетаскиваем элемент')
    def drag_and_drop_element(self, source, target):
        drag_and_drop(self.driver, source, target)

    @allure.step('Кликаем по элементу')
    def click_for_element(self, locator, timeout=30):
        return self.wait_for_element(locator, timeout).click()

    @allure.step('Вводим текст в поле ввода')
    def send_keys_to_input(self, locator, keys, timeout=30):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)
        return element

    @allure.step("Получаем текст элемента")
    def get_text_on_element(self, locator, timeout=30):
        element = self.wait_for_element(locator, timeout)
        return element.text

    @allure.step('Получаем значение атрибута')
    def get_value_attribute(self, locator, attribute, timeout=30):
        element = self.wait_for_element(locator, timeout)
        return element.get_attribute(attribute)

    @allure.step("Получаем url сайта")
    def get_url_site(self):
        WebDriverWait(self.driver, 20).until(EC.url_changes(''))
        return self.driver.current_url




