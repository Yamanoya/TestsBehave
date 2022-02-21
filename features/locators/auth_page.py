from selenium.webdriver.common.by import By


class AuthPageLocators:
    """Локаторы для страницы авторизации"""

    # Кнопка для смены поля телефон на Email
    SWITCH_ON_EMAIL = (By.TAG_NAME, "[data-test='authLoginTypeToggle']")

    # Поле для ввода Email
    FIELD_EMAIL = (By.TAG_NAME, "[name='email']")

    # Поле для ввода пароля
    FIELD_PASSWORD = (By.TAG_NAME, "[name='password']")

    # Кнопка Войти
    ENTER_BUTTON = (By.XPATH, "/html[1]/body[1]/div[1]/main[1]/div[1]/section[1]/div[2]/div[1]/div[1]/div[1]/div[1]/form[1]/div[4]/div[1]/button[1]/span[1]")
