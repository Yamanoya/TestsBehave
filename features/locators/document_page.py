from selenium.webdriver.common.by import By


class DocumentPageLocators:
    """Хранилище базовых локаторов для реестра Документы"""

    # Локатор для импорта документов
    IMPORT_FILE = (By.XPATH, "//input[@type='file']")

    # Локатор для выбора организации
    TAKE_ORGANIZATION = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/main[1]/div[1]/ul[1]/li[1]/div[2]/a[1]/span[1]")

    # Локатор реестра Документы
    RES_DOCUMENTS = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/nav[1]/ul[1]/li[1]/div[1]/button[1]/div[1]")

    # Локатор реестра Черновики
    RES_CHER = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/nav[1]/ul[1]/li[1]/ul[1]/div[1]/div[1]/div[3]/a[1]/div[1]")

    # Локатор Исходящие
    RES_OUTGOING = (By.XPATH, "//a[contains(.,'Исходящие')]")

    # Локатор для получения статусов в Исходящих
    OUTGOING_STATUS = (By.XPATH, "/html[1]/body[1]/div[7]/div[1]/div[1]/div[2]/main[1]/div[1]/ul[1]/li[1]/a[1]/div[4]/span[1]")

    # Локатор для получения текста статуса документа
    STATUS_DOCUMENT = (By.XPATH, "//a/div[4]")

    # Отклонить на форме ввода причины аннулирования
    BUTTON_CANCEL = (By.XPATH, "//form/div[3]/button")

    # Визуализация внутри документа
    VISUALIZATION = (By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/main[1]/div[1]')

    # Локатор для выбора документа
    SELECT_DOCUMENT = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/main[1]/div[1]/ul[1]/li[1]/a[1]")

    # Имя документа внутри
    NAME_DOCUMENT = (By.XPATH, "//nav/div/div")

    # Имя документа после добавления
    NAME_DOCUMENT_AFTER_ADD = (By.XPATH, "//a/div[2]/div[2]")

    # Локатор для кнопки Выбрать получателя
    TAKE_SENDING = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/a[1]")

    # Выбрать контрагента
    TAKE_AGENT = (By.XPATH, "//div/ul/li[2]")

    # Выбрать второго контрагента
    TAKE_SECOND_AGENT = (By.XPATH, "//div[2]/div[2]/div/div/div/ul/li")

    # Локато на кол-во выбратнных агентов
    TAKE_ALL_AGENTS = (By.XPATH, "//div[2]/div[3]/div/div/div/div/div")

    # Кнопка закрытия формы выбора контрагента
    CLOSE_BUTTON = (By.XPATH, "(//button[@type='button'])[14]")

    # Кнопка закрытия формы выбора контрагента, для его удаления
    CLOSE_BUTTON2 = (By.XPATH, "(//button[@type='button'])[13]")

    # Кнопка отправить
    SEND_BUTTON = (By.XPATH, "//span[contains(.,'Отправить')]")

    # Кнопка подтвердить
    ACCEPT_BUTTON = (By.XPATH, "//span[contains(.,'Подтвердить')]")

    # Статус Требуется ответная подпись
    STATUS_WAIT_SIGNATURE = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/main[1]/div[1]/ul[1]/li[1]/a[1]/div[4]/span[1]")

    #Статус требуется ответная подпись внутри документа
    STATUS_WAIT_SIGNATURE_IN_DOCUMENT = (By.XPATH, "//div[@id='root']/div/div/div[2]/nav/div/div[2]")

    # Статус Подписывается
    STATUS_SIGNATURE = (By.XPATH, "//div[@id='root']/div/div/div[2]/main/div/ul/li/div/div[4]")

    # Текст статуса документа после отправки Входящий документ
    INCOMING_DOCUMENT = (By.XPATH, "//span[contains(.,'Обновить список и перейти к документам')]")

    # Кнопка Обновить список и перейти к документам
    BUTTON_REFRESH_LIST = (By.XPATH, "//span[contains(.,'Обновить список и перейти к документам')]")

    # Выбираем документ
    DOCUMENT_ADD_LOCATOR = (By.XPATH, "//a/div[2]/div")

    # Второй документ
    SECOND_DOCUMENT = (By.XPATH, "//li[2]/a/div[4]/span")

    # Кликаем по документу в реестре Входящие
    DOCUMENT_INCOMING = (By.XPATH, "//div[@id='root']/div/div/div[2]/main/div/ul/li/a")

    # Кнопка подписать документ внутри документа
    SIGN_A_DOCUMENT = (By.XPATH, "//span[contains(.,'Подписать документ')]")

    # Ожидаем сообщения после Подписания документа
    SIGN_DOCUMENT_MESSAGE = (By.XPATH, "//div[2]/div[2]/div/div/div/div/div/div/div")

    # Кнопка аннулировать документ
    DECLINE_BUTTON = (By.XPATH, "//button[contains(.,'Аннулировать документ')]")

    # Форма для подтверждения аннулирования
    FORM_FOR_ACCEPT_CANCEL = (By.XPATH, "//h1[contains(.,'Предложение об аннулировании электронного документа')]")

    # Кнопка Подтвердить Аннулирование
    BUTTON_ACCEPT_CANCEL = (By.XPATH, "//span[contains(.,'Подтвердить')]")

    # Поле для ввода причины аннулирования
    FIELD_ACCEPT_CANCEL = (By.XPATH, "//textarea[@name='reason']")

    # Реестр Извещение о получении
    REGISTRY_RECEIPT_NOTICE = (By.XPATH, "//a[contains(.,'Извещение о получении')]")

    # Локатор, статусов документа
    ALL_STATUS = (By.XPATH, "//nav/div/div[2]")

    # Строка с документом и получателями
    DOCUMENT_DRAFT = (By.XPATH, "//main/div/ul/li/div")

    # Форма кол-ва выбранных получателей
    FORM_AGENTS = (By.XPATH, "//a[contains(.,'Получатели')]")

    # Локатор документа в черновиках
    DRAFT_STATUS = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/main[1]/div[1]/ul[1]/li[1]/a[1]/div[4]")

    # Реестр Титул получателя
    REGISTRY_BENEFICIARY_TITLE = (By.XPATH, "//a[contains(.,'Титул получателя')]")

    # Контрагент который выбран в качестве получателя
    TAKING_AGENT = (By.XPATH, "//div[2]/div/div/div/ul/li")

    # Статус внутри документа Завершен
    END_DOCUMENT = (By.XPATH, "//nav/div/div[2]")

    # Всплывающее сообщение после Подтверждения аннулирования
    MESSAGE_ABOUT_CANCEL = (By.XPATH,"//span[contains(.,'Подробнее')]")

    # Реестр у отправителя Предложение об аннулировании
    REGISTER_CANCEL_INGOING = (By.XPATH, "//div[5]/a/div")

    # Кнопка Принять аннулирование у отправителя
    BUTTON_ACCEPT_CANCEL_IN_DOCUMENT = (By.XPATH, "//span[contains(.,'Принять')]")

    # Сообщение Аннулирование одобрено
    CANCEL_IS_OKAY = (By.XPATH, "//div[2]/div/div/div/div/div/div/div/div")

    # Статус документа внутри Аннулирован
    DOCUMENT_IS_CANCEL = (By.XPATH, "//nav/div/div[2]")

    # Ссылка в документе Документ Аннулирован
    DOCUMENT_IS_CANCEL_IN_DOCUMENT = (By.XPATH, "//nav/div/div[2]")

    # Документ в Исходящих в статусе Требуется аннулирование
    DOCUMENT_IN_STATUS_CANCEL = (By.XPATH, "//span[contains(.,'Требуется аннулирование')]")

    # Реестр Предложение об аннулировании
    REGISTER_OFFER_CANCEL = (By.XPATH, "//a[contains(.,'Предложение об аннулировании')]")

    # Кнопка отклонить Аннулирование
    BUTTON_REJECT_CANCEL = (By.XPATH, "//div[2]/button/span/div")

    # Текст Предложение об аннулировании отклонено
    TEXT_CANCEL = (By.XPATH, "//a/div/div")

    # Реестр первичный документ
    REGISTER_NOTIFICATION_DOCUMENT = (By.XPATH, "//a[contains(.,'Уведомление об уточнении')]")

    # Поле с текстом после указания причины отклонения аннулирования
    FIELD_WITH_TEXT_CANCEL = (By.XPATH, "//main/div/div[2]")

    # Поле для ввода причины аннулирования
    FIELD_FOR_ADD_TEXT = (By.XPATH, "//textarea[@name='reason']")

    # Текст для проверки формы для указания причины отклонения
    NOTIFICATION_TEXT = (By.XPATH, "//h1[contains(.,'Уведомление об уточнении электронного документа')]")

    # Кнопка подтвердить Отказ на форме Уведомление об уточнении электронного документа
    BUTTON_ACCEPT_NOTIFICATION_TEXT = (By.XPATH, "//span[contains(.,'Подтвердить')]")

    # Предложение об аннулировани отклонено - Текст в документе после отказания аннулирования
    TEXT_AFTER_REFUSE_CANCEL = (By.XPATH, "/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/main[1]/a[1]/div[1]/div[1]")

    # Реестр Уведомление об уточнении
    REGISTER_NOTIFICATION = (By.XPATH, "//a[contains(.,'Уведомление об уточнении')]")

    # Кнопка для просмотра текста причины отказа аннулирования
    BUTTON_FOR_READ_TEXT_AFTER_REFUSE_CANCEL = (By.XPATH, "(//button[@type='button'])[13]")

    # Кнопка Отклонить документ
    BUTTON_DECLINE = (By.XPATH, "//button[contains(.,'Отклонить документ')]")

    # Форма уведомление об уточнении электронного документа
    NOTIFICATION_FORM = (By.XPATH, "//h1[contains(.,'Уведомление об уточнении электронного документа')]")

    # Статус документа Отклонен
    STATUS_DOCUMENT_DECLINE = (By.XPATH, "//nav/div/div[2]")

    # Флаг Ответная подпись
    FLAG_RESPONSE_SIGNATURE = (By.XPATH, "//span[contains(.,'Ответная подпись')]")

    # Сообщение о 0 байтах
    NULL_BYTES = (By.XPATH, "//li[contains(.,'0ByteNeformal.txt - Размер файла не может быть меньше 1 Байт')]")

    # + еще 1 когда выбираем два получателя
    TWO_RECIPIENTS = (By.XPATH, "//div[3]/div/div[2]/div")

    # Кнопка Отменить
    CANCEL_BUTTON = (By.XPATH, "//form/div[3]/button")

    # Кнопка Отменить, в момент Аннулирования документа
    DECLINE_BUTTON_CANCEL = (By.XPATH, "//button[contains(.,'Отклонить')]")






    # Локатор второго контрагента, чтобы убрать его из получателей

    SECOND_RECIPIENT = (By.XPATH, "//div/ul/li[2]")

    # Локатор Входящего документа у Первого получателя
    FIRST_RECIPIENT = (By.XPATH, "//div/div/div[2]/div/div")

    # Локтаор Входящего документа у Второго получателя
