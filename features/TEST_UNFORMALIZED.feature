Feature: Документ типа Неформализованный

  @flag_off_decline
  @flag_on_decline
  @flag_on_accept
  @flag_on_with_accept_cancel_recipient
  @flag_on_with_decline_cancel_recipient
  @flag_on_with_accept_cancel_sender
  @flag_on_with_decline_cancel_sender
  @sending_two_recipient
  @fixture.browser.chrome
  Scenario: Добавление документа
    Given Переходим на страницу тестируемого стенда
    When Выбираем организацию
    Given Переходим в реестр Черновики
    When Импортируем отчет с именем "Неформалка.txt"
    Then Статус документа "Отсутствует получатель"


  @flag_off_decline
  @fixture.browser.chrome
  Scenario: Отправка документа, без флага ОТВЕТНАЯ ПОДПИСЬ
    Given Переходим в реестр Черновики
    When Выбираем документ
    And Проверяем визуализацию
    When Выбираем получателя, статус документа "Готов к отправке"
    Then Отправляем документ
    And Открылась форма подтверждения Подтвердить и жмем Подтвердить
    When Статус документа в черновиках "Подписывается"
    Then Появляется всплывающее сообщение
    When Открываем Исходящие и проверяем статус "Ожидается извещение о получении"

  @flag_on_with_accept_cancel_recipient
  @flag_on_with_decline_cancel_recipient
  @flag_on_with_accept_cancel_sender
  @flag_on_with_decline_cancel_sender
  @flag_on_accept
  @flag_on_decline
  @fixture.browser.chrome
  Scenario: Отправка документа, с флагом ОТВЕТНАЯ ПОДПИСЬ
    Given Переходим в реестр Черновики
    When Выбираем документ
    And Проверяем визуализацию
    When Выбираем получателя, статус документа "Готов к отправке"
    Then Устанавливаем флаг Ответная подпись
    Then Отправляем документ
    And Открылась форма подтверждения Подтвердить и жмем Подтвердить
    When Статус документа внутри "Подписывается"
    Then Появляется всплывающее сообщение
    When Открываем Исходящие и проверяем статус "Ожидается ответная подпись"


  @flag_on_with_accept_cancel_recipient
  @flag_on_with_decline_cancel_recipient
  @flag_on_with_accept_cancel_sender
  @flag_on_with_decline_cancel_sender
  @flag_on_accept
  @fixture.browser.chrome
  Scenario: Подпись документа на стороне ПОЛУЧАТЕЛЯ
    Given Переходим в реестр входящие со стороны получателя
    When Выбираем документ
    And Статус документа внутри "Требуется ответная подпись"
    Then Проверяем что появилось Извещение о получении
    When Подписываем документ
    And Статус документа внутри "Завершен"
    And Проверяем что появилась кнопка "Аннулировать документ"


  @flag_on_with_decline_cancel_recipient
  @flag_on_with_accept_cancel_recipient
  @fixture.browser.chrome
  Scenario: ДО с аннулированием со стороны ПОЛУЧАТЕЛЯ
    Given Переходим в реестр входящие со стороны получателя
    When Выбираем документ
    And Проверяем что появилась кнопка "Аннулировать документ"
    When Аннулируем документ
    Then Откроется форма Предложение об аннулировании электронного документа
    When Нажимаем Отмена
    When Статус документа внутри "Завершен"
    When Аннулируем документ
    Then Вводим причину аннулирования 123 и Подтверждаем
    When Статус документа внутри "Ожидается аннулирование"

  @flag_on_with_accept_cancel_recipient
  @fixture.browser.chrome
  Scenario: До с аннулированием, принимаем аннулирование  со стороны ПОЛУЧАТЕЛЯ
    Given Переходим в реестр входящие со стороны получателя
    When Выбираем документ
    And Проверяем визуализацию
    When Статус документа внутри "Требуется аннулирование"
    And  Открываем реестр Предложение об аннулировании
    Then Принимаем аннулирование
    Then Аннулирование одобрено
    When Статус документа внутри "Аннулирован"

  @flag_on_with_decline_cancel_recipient
  @fixture.browser.chrome
  Scenario: ДО с аннулированием но не принимаем его со стороны ПОЛУЧАТЕЛЯ
    Given Переходим в реестр входящие со стороны получателя
    When Выбираем документ
    And Проверяем визуализацию
    When Статус документа внутри "Требуется аннулирование"
    When Открываем реестр Предложение об аннулировании
    Then Жмем кнопку Отклонить
    Then Ожидаем появления формы Уведомление об уточнении электронного документа
    When Нажимаем Отмена
    Then Жмем кнопку Отклонить
    Then Вводим причину аннулирования 123 и Подтверждаем
    Then Ожидаем всплывающее сообщения и жмем кнопку подробнее
    When Статус документа внутри "Завершен"

  @flag_on_with_decline_cancel_sender
  @flag_on_with_accept_cancel_sender
  @fixture.browser.chrome
  Scenario: ДО с аннулированием со стороны ОТПРАВИТЕЛЯ
    Given Открыт реестр Исходящих документов со стороны отправителя
    When Выбираем документ
    And Проверяем визуализацию
    And Проверяем что появилась кнопка "Аннулировать документ"
    When Аннулируем документ
    Then Откроется форма Предложение об аннулировании электронного документа
    Then Вводим причину аннулирования 123 и Подтверждаем
    When Статус документа внутри "Ожидается аннулирование"

  @flag_on_with_accept_cancel_sender
  @fixture.browser.chrome
  Scenario: До с аннулированием, принимаем аннулирование со стороны ОТПРАВИТЕЛЯ
    Given Открыт реестр Исходящих документов со стороны отправителя
    When Выбираем документ
    And Проверяем визуализацию
    When Статус документа внутри "Требуется аннулирование"
    And  Открываем реестр Предложение об аннулировании
    Then Принимаем аннулирование
    Then Аннулирование одобрено
    When Статус документа внутри "Аннулирован"


  @flag_on_with_decline_cancel_sender
  @fixture.browser.chrome
  Scenario: ДО с аннулированием но не принимаем его со стороны ОТПРАВИТЕЛЯ
    Given Открыт реестр Исходящих документов со стороны отправителя
    When Выбираем документ
    And Проверяем визуализацию
    When Статус документа внутри "Требуется аннулирование"
    When Открываем реестр Предложение об аннулировании
    Then Жмем кнопку Отклонить
    Then Ожидаем появления формы Уведомление об уточнении электронного документа
    Then Вводим причину аннулирования 123 и Подтверждаем
    Then Ожидаем всплывающее сообщения и жмем кнопку подробнее
    When Статус документа внутри "Завершен"


  @flag_on_decline
  @flag_off_decline
  @fixture.browser.chrome
  Scenario: Отклонение документа со стороны ПОЛУЧАТЕЛЯ
    Given Переходим в реестр входящие со стороны получателя
    When Выбираем документ
    And Проверяем визуализацию
    When Нажимаем кнопку Отклонить документ
    Then Ожидаем форму Уведомление об уточнении
    Then Жмем кнопку Отменить
    When Нажимаем кнопку Отклонить документ
    Then Вводим причину отклонения 123 и нажимаем Принять
    Then Статус документа Отклонен, появится реестр Уведомление об уточнении


  @sending_two_recipient_flag_off
  @fixture.browser.chrome
  Scenario: Отправка документа, без флага ОТВЕТНАЯ ПОДПИСЬ, двум получателям
    Given Переходим в реестр Черновики
    When Выбираем документ
    And Проверяем визуализацию
    When Выбираем получателей, статус документа "Готов к отправке"
    Given Переходим в реестр Черновики
    When У документа два Получателя
    Then Отправляем документ
    And Открылась форма подтверждения Подтвердить и жмем Подтвердить
    When Статус документа внутри "Подписывается"
    Then Появляется всплывающее сообщение

  @sending_two_recipient_flag_on
  @fixture.browser.chrome
  Scenario: Отправка документа, с флагом ОТВЕТНАЯ ПОДПИСЬ, двум получателям
    Given Переходим в реестр Черновики
    When Выбираем документ
    And Проверяем визуализацию
    When Выбираем получателей, статус документа "Готов к отправке"
    Given Переходим в реестр Черновики
    When У документа два Получателя
    Then Устанавливаем флаг Ответная подпись
    Then Отправляем документ
    And Открылась форма подтверждения Подтвердить и жмем Подтвердить
    When Статус документа внутри "Подписывается"
    Then Появляется всплывающее сообщение