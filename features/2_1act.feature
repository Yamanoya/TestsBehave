Feature: Документ типа Акт

  # Добавляем документ
  @add_and_sending_document_act
  @fixture.browser.chrome
  Scenario: Работа с документом типа Акт
    Given В URL есть значение "https://edo-2.cloud.astral-dev.ru/"
    Then Нажимаем на организацию
    And Нажимаем на реестр Документы
    And Нажимаем на Черновики
    Then В URL есть значение "https://edo-2.cloud.astral-dev.ru/0222550a-29d8-4647-94f2-a1f6e34230e0/drafts"
    When Импортируем отчет с именем "DP_REZRUISP_v5_01.xml"
    Then Проверка имени файла "Акт"
    Then Статус документа "Отсутствует получатель"
    Then Кликаем по документу
    Then Проверяем имя документа "Акт № 1 от 29.07.2020"
    When Нажимаем на кнопку Выбрать получателя
    Then Выбираем контрагента
    When Закрываем форму
    Then Нажимаем кнопку отправить
    And Проверяем что открылась форма подтверждения Подтвердить и жмем Подтвердить
    Then Документ в статусе "Подписывается"
    Then Ждем алерт и жмем кнопку
    And Проверяем что документ в статусе Требуется ответная подпись

    # Подписываем документ
  @accept_document_act
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
  @cancel_document_act
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
  @accept_cancel_document_act
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
  @no_accept_cancel_document_act
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
  @decline_document_act
  @fixture.browser.chrome
  Scenario: ДО с отклонением документа
    Given Открыт реестр Входящих документов у получателя
    When Выбираем документ
    When Проверяем наличе кнопки Отклонить документ и нажимаем ее
    Then Ожидаем форму Уведомление об уточнении электронного документа
    And Вводим причину отклонения 123 и нажимаем Принять
    Then Проверяем статус документа Отклонен и появление реестра Уведомление об уточнении