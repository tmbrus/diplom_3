from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    ORDER_CARD = [By.XPATH, '//li[@class="OrderHistory_listItem__2x95r mb-6"][1]']
    NUMBER_ORDER_CARD = [By.XPATH, '//li[@class="OrderHistory_listItem__2x95r mb-6"]'
                                    '//p[@class="text text_type_digits-default"]']
    DATA_WINDOW_ORDER = [By.XPATH, '//p[text()="Cостав"]']
    COUNTER_ORDERS_FOR_ALL_TIME = [By.XPATH, '//div[@class="undefined mb-15"]'
                                             '/p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]']
    COUNTER_ORDERS_FOR_TODAY = [By.XPATH, '//div[@class="OrderFeed_ordersData__1L6Iv"]'
                                          '/div[3]/p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]']
    FEED_HEADER = (By.XPATH, '//h1[contains(text(), "Лента заказов")]')

    @staticmethod
    def number_our_order(number):
        return [By.XPATH, f'//li[text()="{number}"]']

    @staticmethod
    def search_card_order_for_number(number):
        return [By.XPATH, f'//li[@class="OrderHistory_listItem__2x95r mb-6"]//p[text()="{number}"]']