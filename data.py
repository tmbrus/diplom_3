class Ingredients:

    @staticmethod
    def ingredients_body():
        bun = '61c0c5a71d1f82001bdaaa6c'
        main = '61c0c5a71d1f82001bdaaa6e'
        souse = '61c0c5a71d1f82001bdaaa73'
        return { 'ingredients': [bun, main, souse]}

class TestData:
    DESIGNER_TITLE = 'Соберите бургер'
    ORDER_FEED_TITLE = 'Лента заказов'
    INGREDIENT_DETAILS_TITLE = 'Детали ингредиента'
    INGREDIENT_COUNTER_AFTER_ADD = '2'
