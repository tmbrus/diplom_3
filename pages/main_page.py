import allure
from locators.main_page_locators import ManePageLocators
from pages.base_page import BasePage


class ManePage(BasePage):

    @allure.step('Ждём загрузки главной страницы')
    def main_page_loading_wait(self):
        self.wait_for_element_hide(ManePageLocators.OVERLAY)

    @allure.step('Кликаем на "Личный кабинет"')
    def click_for_personal_account(self):
        self.click_for_element(ManePageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Кликаем на "Конструктор"')
    def click_for_designer(self):
        self.click_for_element(ManePageLocators.DESIGNER_BUTTON)

    @allure.step('Кликаем на "Лента заказов"')
    def click_for_orders_feed(self):
        self.click_for_element(ManePageLocators.ORDER_FEED_BUTTON)

    @allure.step('Кликаем на "Ингредиент"')
    def click_for_ingredient(self):
        self.click_for_element(ManePageLocators.BURGER_INGREDIENT)

    @allure.step('Кликаем на крестик в сплывающем окне ингредиента')
    def click_for_close_button_ingredient_card(self):
        self.click_for_element(ManePageLocators.CLOSE_BURGER_INGREDIENT_CARD)

    @allure.step('Перетаскиваем ингредиент в корзину')
    def put_ingredient_into_basket(self):
        ingredient = self.wait_for_element(ManePageLocators.BURGER_INGREDIENT)
        basket = self.wait_for_element(ManePageLocators.BASKET)
        self.drag_and_drop_element(ingredient, basket)

    @allure.step('Получаем текст счётчика ингредиента')
    def get_text_counter_ingredient(self):
        return self.get_text_on_element(ManePageLocators.COUNTER_INGREDIENT)

    @allure.step('Кликаем по кнопке "Оформить заказ"')
    def click_button_arrange_order(self):
        self.click_for_element(ManePageLocators.ARRANGE_ORDER_BUTTON)

    @allure.step('Получаем текст заголовка Конструктора')
    def get_text_headline_designer(self):
        return self.get_text_on_element(ManePageLocators.HEADLINE_ASSEMBLE_BURGER)

    @allure.step('Получаем текст заголовка Лента заказов')
    def get_text_headline_order_feed(self):
        return self.get_text_on_element(ManePageLocators.HEADLINE_ORDER_FEED)

    @allure.step('Получаем текст заголовка окна ингредиента')
    def get_text_headline_details_ingredient(self):
        return self.get_text_on_element(ManePageLocators.HEADLINE_DETAILS_INGREDIENT)

    @allure.step('Получаем текст окна оформления заказа')
    def get_text_window_arrange_order(self):
        return self.get_text_on_element(ManePageLocators.TEXT_WINDOW_ORDER)

    @allure.step('Получаем номер заказа из всплывающего окна')
    def get_order_number(self):
        order_number_element = self.wait_for_element(ManePageLocators.ORDER_NUMBER)
        return order_number_element.text.replace('#', '')




