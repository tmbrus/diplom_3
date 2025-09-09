from selenium.webdriver.common.by import By


class ManePageLocators:
    OVERLAY = [By.XPATH, './/div[contains(@class, "Modal_modal_overlay__x2ZCr")]/parent::div']
    DESIGNER_BUTTON = [By.XPATH, './/p[normalize-space()="Конструктор"]']
    ORDER_FEED_BUTTON = [By.XPATH, './/p[normalize-space()="Лента Заказов"]']
    PERSONAL_ACCOUNT_BUTTON = [By.XPATH, './/p[normalize-space()="Личный Кабинет"]']
    BURGER_INGREDIENT = [By.XPATH, './/img[@alt="Флюоресцентная булка R2-D3"]']
    CLOSE_BURGER_INGREDIENT_CARD = [By.CSS_SELECTOR, '.Modal_modal__close_modified__3V5XS']
    COUNTER_INGREDIENT = [
        By.XPATH,
        './/a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]//p[contains(@class,"counter_counter__num__")]'
    ]
    BASKET = [By.XPATH, './/div[contains(@class, "BurgerConstructor_basket__totalContainer")]']
    HEADLINE_ASSEMBLE_BURGER = [By.XPATH, './/h1[normalize-space()="Соберите бургер"]']
    HEADLINE_ORDER_FEED = [By.XPATH, './/h1[normalize-space()="Лента заказов"]']
    HEADLINE_DETAILS_INGREDIENT = [By.XPATH, './/h2[normalize-space()="Детали ингредиента"]']
    TEXT_WINDOW_ORDER = [By.XPATH, './/p[normalize-space()="Ваш заказ начали готовить"]']
    ORDER_NUMBER = [By.XPATH, './/h2[contains(@class, "Modal_modal__title")]']
    ARRANGE_ORDER_BUTTON = [
        By.XPATH,
        './/button[contains(@class, "button_button__") and contains(@class, "button_button_type_primary__") and '
        'contains(@class, "button_button_size_large__")]'
    ]
