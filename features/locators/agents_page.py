from selenium.webdriver.common.by import By

class AgentsLocators:


    # Список Контрагенты
    AGENTS_LIST = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/nav[1]/ul[1]/li[2]/div[1]/button[1]/div[1]")

    # Раздел Мои контрагенты
    MY_AGENTS_LIST = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/nav[1]/ul[1]/li[2]/ul[1]/div[1]/div[1]/div[1]/a[1]/div[1]")

    # Кнопка Добавить Контрагента
    ADD_MY_AGENT_BUTTON = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/nav[1]/a[1]/span[1]/div[1]")

    # Поле поиска агента
    MY_AGENTS_FIELD_SEARCH = (By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[2]/div[1]/div[1]/div[1]/input[1]")

    # Форма добавление контрагента
    FORM_ADD_AGENT = (By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/h2[1]")

    # Отравить приглашение агенту
    MY_AGENTS_SEND_INVITE_AGENT = (By.XPATH,"/html[1]/body[1]/div[2]/div[3]/div[2]/div[3]/ul[1]/li[1]/div[3]/div[1]/div[1]/button[1]/span[1]/*[name()='svg'][1]")

    # Кнопка Обновить список и перейти к контрагентам
    MY_AGENTS_REFRESH_LIST_BUTTON = (By.XPATH,"/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]/span[1]")

    # Кнопка Обновить список и перейти к кнотрагентам
    MY_AGENTS_REFRESH_LIST_BUTTON_ABOUT = (By.XPATH,"/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]/span[1]")

    # Общий Чекбокс
    INVITE_CHECKBOX_BUTTON = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/main[1]/div[1]/ul[1]/li[1]/div[2]/div[1]/div[1]/button[1]/span[1]/*[name()='svg'][1]")

    # Запись _Тест3_
    NAME_AGENT = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/main[1]/div[1]/ul[1]/li[1]/div[1]/div[2]/div[1]/div[1]/span[1]")

    # Кнопка Принять
    INVITE_ACCEPT_BUTTON = (By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/main[1]/div[1]/ul[1]/li[1]/div[2]/div[1]/div[1]/button[1]/span[1]/*[name()='svg'][1]")

    # Кол-во Исходящих, в разделе Приглашения
    INVITE_INPUT_OUTBOX = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/nav[1]/div[1]/a[2]/div[1]")

    # Кол-во Входящих, в разделе Приглашения
    INVITE_INPUT_INVITATION = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/main[1]/div[1]/ul[1]/li[1]/div[1]/div[2]/div[1]/div[1]/span[1]/font[1]/font[1]")

    # Кнопка Отклонить
    INVITE_BUTTON_DECLINE = (By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/nav[1]/div[1]/div[2]/div[2]/div[1]/button[1]/span[1]/*[name()='svg'][1]")

    # Кнопка заблокировать
    INVITE_BUTTON_BLOCK = (By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/nav[1]/div[1]/div[2]/div[3]/div[1]/button[1]/span[1]/*[name()='svg'][1]")

    # Кол-во агентов, в разделе Мои контрагенты, счетчик
    MY_AGENTS_VALUE = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/nav[1]/div[1]/div[1]/div[1]")

    # Раздел Черный список
    CH_AGENTS = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/nav[1]/ul[1]/li[2]/ul[1]/div[1]/div[1]/div[3]/a[1]/div[1]")

    # Кнопка разблокировать
    CH_AGENTS_BUTTON_UNBLOCK = (By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/nav[1]/div[1]/div[3]/div[1]/div[1]/button[1]/span[1]/*[name()='svg'][1]")


    # Кол-во агнетов в Моих Контрагентах
    VALUE_AGENTS_AT_MY_AGENTS = (By. XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/nav[1]/div[1]/div[1]/div[1]")

    # Кнопка удалить
    DELETE_AGENT = (By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/main[1]/div[1]/ul[1]/li[1]/div[1]/div[1]/div[1]/button[1]/span[1]/*[name()='svg'][1]")
