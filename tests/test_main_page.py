import allure
from pages.main_page import ManePage



class TestMainPage:

    @allure.title('Переход по клику на "Конструктор"')
    def test_transition_by_click_for_designer(self, driver):
        main_page = ManePage(driver)
        main_page.main_page_loading_wait()
        main_page.click_for_designer()
        expected_result = 'Соберите бургер'
        actual_result = main_page.get_text_headline_designer()
        assert actual_result == expected_result

    @allure.title('Переход по клику на раздел "Лента заказов"')
    def test_transition_by_click_for_order_feed(self, driver):
        main_page = ManePage(driver)
        main_page.main_page_loading_wait()
        main_page.click_for_orders_feed()
        expected_result = 'Лента заказов'
        actual_result = main_page.get_text_headline_order_feed()
        assert actual_result == expected_result

    @allure.title('Открывается окно с деталями по клику на ингредиент')
    def test_open_window_details_by_click_on_ingredient(self, driver):
        main_page = ManePage(driver)
        main_page.main_page_loading_wait()
        main_page.click_for_ingredient()
        expected_result = 'Детали ингредиента'
        actual_result = main_page.get_text_headline_details_ingredient()
        assert actual_result == expected_result

    @allure.title('Всплывающее окно с деталями ингредиента закрывается кликом по крестику')
    def test_window_details_ingredient_closes_by_click_on_cross(self, driver):
        main_page = ManePage(driver)
        main_page.main_page_loading_wait()
        main_page.click_for_ingredient()
        main_page.click_for_close_button_ingredient_card()
        expected_result = 'Соберите бургер'
        actual_result = main_page.get_text_headline_designer()
        assert actual_result == expected_result

    @allure.title('Проверяем, что при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    def test_counter_increases_by_adding_in_order(self, driver):
        main_page = ManePage(driver)
        main_page.main_page_loading_wait()
        main_page.put_ingredient_into_basket()
        expected_result = '2'
        actual_result = main_page.get_text_counter_ingredient()
        assert actual_result == expected_result