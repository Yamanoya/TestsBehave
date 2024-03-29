Feature: Документ типа Неформализованный. Только проверки не входящие в основной сценарий

  @flag_off_decline_other
  @fixture.browser.chrome
  Scenario: Отправка документа, без флага ОТВЕТНАЯ ПОДПИСЬ
    Given Переходим в реестр Черновики
    When Выбираем документ
    And Проверяем визуализацию
    When Выбираем получателя, статус документа "Готов к отправке"
    And Убираем получателя "Получатели (1)",статус документа Отсутствует получатель
    When Выбираем получателя, статус документа "Готов к отправке"
    Then Отправляем документ
    And Открылась форма подтверждения Подтвердить и жмем Подтвердить
    When Статус документа в черновиках "Подписывается"
    Then Появляется всплывающее сообщение
    When Открываем Исходящие и проверяем статус "Ожидается извещение о получении"


  @sending_two_recipient_flag_off_other
  @fixture.browser.chrome
  Scenario: Отправка документа, без флага ОТВЕТНАЯ ПОДПИСЬ, двум получателям
    Given Переходим в реестр Черновики
    When Выбираем документ
    And Проверяем визуализацию
    When Выбираем получателей, статус документа "Готов к отправке"
    Given Переходим в реестр Черновики
    When У документа два Получателя
    And Убираем получателей "Получатели (2)",статус документа Отсутствует получатель
    When Выбираем получателей, статус документа "Готов к отправке"
    Then Отправляем документ
    And Открылась форма подтверждения Подтвердить и жмем Подтвердить
    When Статус документа внутри "Подписывается"
    Then Появляется всплывающее сообщение
