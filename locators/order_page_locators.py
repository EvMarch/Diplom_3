from selenium.webdriver.common.by import By

class OrderPageLocators:
    # локатор кнопки «Заказать» в шапке страницы
    ORDER_UP_BUTTON = [By.XPATH, ".//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']"]

    # локатор кнопки «Заказать» в середине страницы
    ORDER_DOWN_BUTTON = [By.XPATH, ".//button[contains(@class, 'Button_Button__ra12g Button_Middle__1CSJM') and text() = 'Заказать']"]

