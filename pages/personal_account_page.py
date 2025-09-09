import allure
from locators.personal_account_page_locators import PersonalAccountPageLocators
from pages.base_page import BasePage


class PersonalAccountPage(BasePage):

    @allure.step('Вводим email')
    def send_email(self, email):
        self.send_keys_to_input(PersonalAccountPageLocators.EMAIL_INPUT, email)

    @allure.step('Вводим пароль')
    def send_password(self, password):
        self.send_keys_to_input(PersonalAccountPageLocators.PASSWORD_INPUT, password)

    @allure.step('Нажимаем кнопку "Войти"')
    def click_enter_button(self):
        self.click_for_element(PersonalAccountPageLocators.ENTER_BUTTON)

    @allure.step('Получаем текст кнопки "Войти"')
    def get_text_enter_button(self):
        return self.get_text_on_element(PersonalAccountPageLocators.ENTER_BUTTON)