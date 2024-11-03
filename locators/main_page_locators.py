from selenium.webdriver.common.by import By

class MainPageLocators:
    # Логотип Stellar Burgers
    LOGO = ".//a"
    # Кнопка «Конструктор»
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[contains(text(), 'Конструктор')]")
    # Кнопка «Личный кабинет»
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, ".//p[contains(text(), 'Личный Кабинет')]")
    # Кнопка «Лента заказов»
    ORDER_FEED_BUTTON = (By.XPATH, ".//p[contains(text(), 'Лента Заказов')]")


    # Форма ленты заказа
    ORDER_FEED_FORM = (By.XPATH, ".//div[@class = 'OrderFeed_orderFeed__2RO_j']")
    # Форма конструктора
    CONSTRUCTOR_FORM = (By.XPATH, ".//div[@class = 'BurgerIngredients_ingredients__menuContainer__Xu3Mo']")
    # Кнопка оформить заказ
    ORDER_BUTTON = (By.XPATH, ".//button[text() = 'Оформить заказ']")
    # Кнопка флюорисцентной булки
    FLU_BUN_BUTTON = (By.XPATH, ".//img[@alt = 'Флюоресцентная булка R2-D3']")
    # Крестик на модульном окне
    CLOSE_POPUP_FORM = (By.XPATH, '//button[contains(@class,"close")]')
    # Счетчик ингредиента
    COUNTER_INGREDIENT = (By.XPATH, ".//p[contains(@class, 'counter_counter__num__3nue1')]")
    # Форма оформленного заказа
    ORDER_FORM = (By.XPATH, ".//div[@class = 'Modal_modal__container__Wo2l_']")
    # Корзина
    ORDER_BASKET = (By.XPATH, ".//div[contains(@class, 'constructor-element_pos_top')]")
    # Номер заказа
    ORDER_NUMBER = (By.XPATH, ".//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq')]")
    # Кнопка личного кабинета
    ACCOUNT_BUTTON = (By.XPATH, ".//button[contains(text(), 'Войти в аккаунт')]")
    # Форма флюорисцентной булки
    INGREDIENTS_POPUP_FORM = (By.XPATH, "//h2[text()= 'Детали ингредиента']")



