BASE_URL = 'https://stellarburgers.nomoreparties.site'

# Web URLs
MANE_SITE = BASE_URL
ORDER_HISTORY_URL = f'{BASE_URL}/account/order-history'
FEED_URL = f'{BASE_URL}/feed'

class ApiUrl:
    BASE_URL = BASE_URL
    CREATING_USER_URL = f'{BASE_URL}/api/auth/register'
    CREATING_ORDER_URL = f'{BASE_URL}/api/orders'
    DELETE_USER_URL = f'{BASE_URL}/api/auth/user'
    LOGIN_URL = f'{BASE_URL}/api/auth/login'
    USER_URL = f'{BASE_URL}/api/auth/user'
    INGREDIENTS_URL = f'{BASE_URL}/api/ingredients'