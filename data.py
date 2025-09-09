class Ingredients:

    @staticmethod
    def ingredients_body():
        bun = '61c0c5a71d1f82001bdaaa6c'
        main = '61c0c5a71d1f82001bdaaa6e'
        souse = '61c0c5a71d1f82001bdaaa73'
        return { 'ingredients': [bun, main, souse]}

class ApiUrl:
    BASE_URL = 'https://stellarburgers.nomoreparties.site'
    CREATING_USER_URL = '/api/auth/register'
    CREATING_ORDER_URL = '/api/orders'
    DELETE_USER_URL = '/api/auth/user'
