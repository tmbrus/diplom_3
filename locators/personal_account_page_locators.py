from selenium.webdriver.common.by import By


class PersonalAccountPageLocators:
    EMAIL_INPUT = (By.XPATH, '//input[@name="name"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@name="Пароль"]')
    ENTER_BUTTON = (By.XPATH, '//button[text()="Войти"]')