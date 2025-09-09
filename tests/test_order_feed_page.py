import allure
from helper import CreatedOrder
from pages.order_feed_page import OrderFeedPage
from pages.main_page import ManePage
from pages.personal_account_page import PersonalAccountPage


class TestOrderFeedPage:


    @allure.title('При создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    def test_when_creating_new_order_completed_in_all_time_counter_increases(self, driver, creating_user):
        main_page = ManePage(driver)
        account_page = PersonalAccountPage(driver)
        order_page = OrderFeedPage(driver)
        main_page.main_page_loading_wait()
        token, email, password = creating_user
        main_page.click_for_personal_account()
        account_page.send_email(email)
        account_page.send_password(password)
        account_page.click_enter_button()
        main_page.main_page_loading_wait()
        main_page.click_for_orders_feed()
        number_orders = order_page.get_data_counter_orders_for_all_time()
        CreatedOrder.created_order(token)
        expected_result = str(int(number_orders) + 1)
        actual_result = order_page.get_data_counter_orders_for_all_time()

        # Проверяем что счётчик "Выполнено за всё время" увеличился после оформления заказ
        # (для стабильности UI теста, заказ создаётся через API)
        assert actual_result == expected_result

    @allure.title('При создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    def test_when_creating_order_the_completed_today_counter_increases(self, driver, creating_user):
        main_page = ManePage(driver)
        account_page = PersonalAccountPage(driver)
        order_page = OrderFeedPage(driver)
        main_page.main_page_loading_wait()
        token, email, password = creating_user
        main_page.click_for_personal_account()
        account_page.send_email(email)
        account_page.send_password(password)
        account_page.click_enter_button()
        main_page.main_page_loading_wait()
        main_page.click_for_orders_feed()
        number_orders = order_page.get_data_counter_for_today()
        CreatedOrder.created_order(token)
        expected_result = str(int(number_orders) + 1)
        actual_result = order_page.get_data_counter_for_today()

        # Проверяем что счётчик "Выполнено за сегодня" увеличился после оформления заказ
        # (для стабильности UI теста, заказ создаётся через API)
        assert actual_result == expected_result

    @allure.title('При создании заказа он появляется в разделе "В работе"')
    def test_when_an_order_is_created_it_appears_in_the_in_progress_section(self, driver, creating_user):
        main_page = ManePage(driver)
        account_page = PersonalAccountPage(driver)
        order_page = OrderFeedPage(driver)
        main_page.main_page_loading_wait()
        token, email, password = creating_user
        main_page.click_for_personal_account()
        account_page.send_email(email)
        account_page.send_password(password)
        account_page.click_enter_button()
        main_page.main_page_loading_wait()
        main_page.click_for_orders_feed()
        order_page.get_data_counter_orders_for_all_time()
        number = CreatedOrder.created_order(token)
        actual_result = order_page.get_order_in_works_number(number)
        expected_result = f'0{number}'

        # Проверяем что после оформления заказа его номер появился "В работе"
        # (для стабильности UI теста, заказ создаётся через API)
        assert actual_result == expected_result
