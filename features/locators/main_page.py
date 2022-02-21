from selenium.webdriver.common.by import By


class ManePageLocators:
    """Хранилище локаторов главной страницы, аналог BasePageLocators но только для главной страницы.
    т.е. тут хранятся толкьо те локаторы которые есть на главной и больше нигде!"""

    # Локатор виджетов на главной странице (не реализован в тестах, поэтому не актуальный)
    VIDGETS = (By. XPATH, 'test')


    SEARCH_FIELD = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/header[1]/div[2]/div[1]/input[1]")


    COUNT_ORGANIZATIONS = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/nav[1]/div[1]/div[1]/div[1]")


