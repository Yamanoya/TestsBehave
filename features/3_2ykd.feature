@document_ykd
Feature: Документ типа УПД

    # Добавляем документ и отправляем его
  @add_and_sending_document_ykd
  @fixture.browser.chrome
  Scenario Template: Работа с документом типа УКД с разными функциями
    Given В URL есть значение "https://edo-2.cloud.astral-dev.ru/"
    Then Нажимаем на организацию
    And Нажимаем на реестр Документы
    And Нажимаем на Черновики
    Then В URL есть значение "https://edo-2.cloud.astral-dev.ru/dcbf5864-b9cb-4ec7-801d-0e7a831b6bc2/drafts"
    When Импортируем отчет с именем "<name>"
    ####Then Проверка имени файла "Торг-12"
    Then Статус документа "Отсутствует получатель"
    Then Кликаем по документу
    ###########Then Проверяем имя документа "Торг-12 № 1 от 29.07.2020"
    When Нажимаем на кнопку Выбрать получателя
    Then Выбираем контрагента
    When Закрываем форму
    Then Нажимаем кнопку отправить
    And Проверяем что открылась форма подтверждения Подтвердить и жмем Подтвердить
    Then Документ в статусе "Подписывается"
    Then Ждем алерт и жмем кнопку
    And Проверяем что документ в статусе Требуется ответная подпись
    Examples:
      | name |
      | ON_NKORSCHFDOPPR_2AE443745C8-1E68-4FBB-B893-227DED199E1D_2AEDA0511BD-14F9-493C-8F60-88D21CAB5E78_20211021_79230efb-c773-494c-b5d9-573e4defd46c.xml |
      | ON_NKORSCHFDOPPR_2AE443745C8-1E68-4FBB-B893-227DED199E1D_2AEDA0511BD-14F9-493C-8F60-88D21CAB5E78_20211021_68355109-5f6a-4397-b4f0-90c2efef53e4.xml |

    # Подписываем документ
  @accept_document_ykd
  @fixture.browser.chrome
  Scenario: ДО с подписью документа
    Given Открыт реестр Входящих документов у получателя
    When Выбираем документ
    Then Проверяем что документ внутри в статусе Требуется ответная подпись
    When Нажимаем подписать документ
    Then Ожидаем всплывающее сообщение
    Then Появляется кнопка Аннулировать и документ в статусе Завершен
    Then Проверяем что появились Извещение о получении и Титул получателя
    Then Проверяем внутри документа статус Завершен

    # Аннулируем документ
  @cancel_document_ykd
  @fixture.browser.chrome
  Scenario: ДО с аннулированием
    Given Открыт реестр Входящих документов у получателя
    When Выбираем документ
    Then Проверяем что документ внутри в статусе Завершен
    When Нажимаем на кнопку Аннулировать документ
    Then Откроется форма Предложение об аннулировании электронного документа
    And Вводим причину аннулирования 123 и нажимаем Принять
    Then Ожидаем всплывающее сообщение об аннуровании и нажимаем подробнее
    Then Проверяем наличие текста Требуется аннулирование


    # Подтверждаем аннулирование документа со стороны отправителя
  @accept_cancel_document_ykd
  @fixture.browser.chrome
  Scenario: До с аннулированием, принимаем аннулирование
    Given Открыт реестр Исходящих документов со стороны отправителя
    When Кликаем по документу в статусе Требуется аннулирование
    And Переходим в реестр Предложение об аннулировании
    Then Нажимаем Принять аннулирование
    Then Аннулирование одобрено
    Then Статус документа Аннулирован
    Then Ссылка в документе Документ аннулирован


    # Отклоняем аннулирование со стороны отправителя
  @no_accept_cancel_document_ykd
  @fixture.browser.chrome
  Scenario: ДО с аннулированием но не принимаем его со стороны отправителя
    Given Открыт реестр Исходящих документов со стороны отправителя
    When Кликаем по документу в статусе Требуется аннулирование
    When Переходим в реестр Предложение об аннулировании
    Then Жмем кнопку Отклонить
    Then Ожидаем появления формы Уведомление об уточнении электронного документа
    And Вводим причину аннулирования 123 и нажимаем Принять
    Then Ожидаем всплывающее сообщения и жмем кнопку подробнее
    Then Проверяем внутри документа статус Завершен
    Then Переходим в реестр Уведомление об уточнении
    Then Переходим в режим чтения текста и видим текст 123

    # Отклоняем документ
  @decline_document_ykd
  @fixture.browser.chrome
  Scenario: ДО с отклонением документа
    Given Открыт реестр Входящих документов у получателя
    When Выбираем документ
    When Проверяем наличе кнопки Отклонить документ и нажимаем ее
    Then Ожидаем форму Уведомление об уточнении электронного документа
    And Вводим причину отклонения 123 и нажимаем Принять
    Then Проверяем статус документа Отклонен и появление реестра Уведомление об уточнении