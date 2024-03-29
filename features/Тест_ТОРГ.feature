Feature: Документ типа Торг-12

  # Добавляем документ и отправляем его
  @torg_all_decline_accept
  @torg_all_decline_cancel
  @torg_all_cancel
  @fixture.browser.chrome
  Scenario: Работа с документом типа Торг-12
    Given Переходим на страницу тестируемого стенда
    Then Нажимаем на организацию
    Then Переходим в реестр Документы -> Черновики
    When Импортируем отчет с именем "DP_TOVTORGPR_v5_01.xml"
    Then Проверка имени файла "Торг-12"
    Then Статус документа "Отсутствует получатель"
    When Выбираем документ
    Then Проверяем имя документа "Торг-12 № 1 от 29.07.2020"
    When Выбираем получателя
    Then Отправляем документ
    And Открылась форма подтверждения Подтвердить и жмем Подтвердить




  @torg_all_decline_accept
  @torg_all_decline_cancel
  @fixture.browser.chrome
  Scenario: ДО с подписью документа
    Given Переходим в реестр входящие со стороны получателя
    When Выбираем документ
    Then Статус документа "Требуется ответная подпись"
    When Подписываем документ
    Then Ожидаем всплывающее сообщение "Документ подписан"
    Then Появляется кнопка Аннулировать и документ в статусе Завершен
    Then Проверяем что появились Извещение о получении и Титул получателя
    Then Проверяем внутри документа статус Завершен


    # Аннулируем документ
  @torg_all_decline_accept
  @torg_all_decline_cancel
  @fixture.browser.chrome
  Scenario: ДО с аннулированием
    Given Переходим в реестр входящие со стороны получателя
    When Выбираем документ
    Then Статус документа "Завершен"
    When Аннулируем документ
    Then Откроется форма Предложение об аннулировании электронного документа
    And Вводим причину отклонения 123 и нажимаем Принять
    Then Ожидаем всплывающее сообщение об Аннулировании и нажимаем Подробнее
    When Проверяем наличие текста Требуется аннулирование


    # Подтверждаем аннулирование документа со стороны отправителя
  @torg_all_decline_accept
  @fixture.browser.chrome
  Scenario: До с аннулированием, принимаем аннулирование
    Given Открыт реестр Исходящих документов со стороны отправителя
    When Выбираем документ
    And  Открываем реестр Предложение об аннулировании
    Then Принимаем аннулирование
    Then Аннулирование одобрено
    Then Статус документа Аннулирован
    Then Ссылка в документе Документ аннулирован


    # Отклоняем аннулирование со стороны отправителя
  @torg_all_decline_cancel
  @fixture.browser.chrome
  Scenario: ДО с аннулированием но не принимаем его со стороны отправителя
    Given Открыт реестр Исходящих документов со стороны отправителя
    When Выбираем документ в статусе Требуется аннулирование
    When Открываем реестр Предложение об аннулировании
    Then Жмем кнопку Отклонить
    Then Ожидаем появления формы Уведомление об уточнении электронного документа
    And  Вводим причину аннулирования 123 и Подтверждаем
    Then Ожидаем всплывающее сообщения и жмем кнопку подробнее
    Then Проверяем внутри документа статус Завершен


    # Отклоняем документ
  @torg_all_cancel
  @fixture.browser.chrome
  Scenario: ДО с отклонением документа
    Given Переходим в реестр входящие со стороны получателя
    When Выбираем документ
    When Нажимаем кнопку Отклонить документ
    Then Ожидаем форму Уведомление об уточнении
    And Вводим причину отклонения 123 и нажимаем Принять
    Then Статус документа Отклонен, появится реестр Уведомление об уточнении