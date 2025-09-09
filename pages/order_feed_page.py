import allure
from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.base_page import BasePage



class OrderFeedPage(BasePage):

    @allure.step('Получаем данные счётчика "За всё время"')
    def get_data_counter_orders_for_all_time(self):
        return self.get_text_on_element(OrderFeedPageLocators.COUNTER_ORDERS_FOR_ALL_TIME)

    @allure.step('Получаем данные счётчика "За сегодня"')
    def get_data_counter_for_today(self):
        return self.get_text_on_element(OrderFeedPageLocators.COUNTER_ORDERS_FOR_TODAY)

    @allure.step('Получаем номер заказа в разделе "В работе"')
    def get_order_in_works_number(self, number):
        return self.get_text_on_element(OrderFeedPageLocators.number_our_order(number))

    @allure.step('Получаем номер нашего заказа из "Лента заказов"')
    def get_number_our_order_in_the_feed_orders(self, number):
        return self.get_text_on_element(OrderFeedPageLocators.search_card_order_for_number(number))

    @allure.step('Получаем номер заказа')
    def get_number_order(self):
        return self.get_text_on_element(OrderFeedPageLocators.NUMBER_ORDER_CARD)

    @allure.step('Кликаем по карточке заказа')
    def click_order_card(self):
        self.click_for_element(OrderFeedPageLocators.ORDER_CARD)

    @allure.step('Получаем данные окна заказа')
    def get_data_window_order(self):
        return self.get_text_on_element(OrderFeedPageLocators.DATA_WINDOW_ORDER)