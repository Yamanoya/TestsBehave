@document_ypd
Feature: Документ типа УПД



  @YPD_ALL_ACCEPT_DECLINE
  @fixture.browser.chrome
  Scenario Template: ДО УПД, с принятием аннулирования со стороны отправителя
    Given Переходим на страницу тестируемого стенда
    Then Нажимаем на организацию
    Then Переходим в реестр Документы -> Черновики
    Then Произошел редирект на страницу "https://edo-2.cloud.astral-dev.ru/dcbf5864-b9cb-4ec7-801d-0e7a831b6bc2/drafts"
    When Импортируем отчет с именем "<name>"
    Then Статус документа "Отсутствует получатель"
    When Выбираем документ
    When Выбираем получателя
    Then Отправляем документ
    And Открылась форма подтверждения Подтвердить и жмем Подтвердить
    Then Проверяем статус документа "Подписывается"

    Given Переходим в реестр входящие со стороны получателя
    When Выбираем документ
    Then Статус документа "Требуется ответная подпись"
    When Подписываем документ
    Then Ожидаем всплывающее сообщение "Документ подписан"
    Then Появляется кнопка Аннулировать и документ в статусе Завершен
    Then Проверяем что появились Извещение о получении и Титул получателя
    Then Проверяем внутри документа статус Завершен

    Given Переходим в реестр входящие со стороны получателя
    When Выбираем документ
    Then Статус документа "Завершен"
    When Аннулируем документ
    Then Откроется форма Предложение об аннулировании электронного документа
    And Вводим причину отклонения 123 и нажимаем Принять
    Then Ожидаем всплывающее сообщение об Аннулировании и нажимаем Подробнее
    When Проверяем наличие текста Требуется аннулирование

    Given Открыт реестр Исходящих документов со стороны отправителя
    When Выбираем документ в статусе Требуется аннулирование
    When Открываем реестр Предложение об аннулировании
    Then Принимаем аннулирование
    Then Аннулирование одобрено
    Then Статус документа Аннулирован
    Then Ссылка в документе Документ аннулирован

    Examples:
      | name |
      | ON_NSCHFDOPPR_2AE443745C8-1E68-4FBB-B893-227DED199E1D_2AEDA0511BD-14F9-493C-8F60-88D21CAB5E78_20211021_d92c4ba7-f375-4668-b4f6-ff8915a0472c.xml |
      | ON_NSCHFDOPPR_2AE443745C8-1E68-4FBB-B893-227DED199E1D_2AEDA0511BD-14F9-493C-8F60-88D21CAB5E78_20211112_241d7630-004a-4e20-abf7-946d4fe58aa8.xml |



  @YPD_ALL_CANCEL_DECLINE
  @fixture.browser.chrome
  Scenario Template: ДО УПД, с отклонением аннулирования со стороны отправителя
    Given Переходим на страницу тестируемого стенда
    Then Нажимаем на организацию
    Then Переходим в реестр Документы -> Черновики
    Then Произошел редирект на страницу "https://edo-2.cloud.astral-dev.ru/dcbf5864-b9cb-4ec7-801d-0e7a831b6bc2/drafts"
    When Импортируем отчет с именем "<name>"
    Then Статус документа "Отсутствует получатель"
    When Выбираем документ
    When Выбираем получателя
    Then Отправляем документ
    And Открылась форма подтверждения Подтвердить и жмем Подтвердить
    Then Проверяем статус документа "Подписывается"

    Given Переходим в реестр входящие со стороны получателя
    When Выбираем документ
    Then Статус документа "Требуется ответная подпись"
    When Подписываем документ
    Then Ожидаем всплывающее сообщение "Документ подписан"
    Then Появляется кнопка Аннулировать и документ в статусе Завершен
    Then Проверяем что появились Извещение о получении и Титул получателя
    Then Проверяем внутри документа статус Завершен

    Given Переходим в реестр входящие со стороны получателя
    When Выбираем документ
    Then Статус документа "Завершен"
    When Аннулируем документ
    Then Откроется форма Предложение об аннулировании электронного документа
    And Вводим причину отклонения 123 и нажимаем Принять
    Then Ожидаем всплывающее сообщение об Аннулировании и нажимаем Подробнее
    When Проверяем наличие текста Требуется аннулирование

    Given Открыт реестр Исходящих документов со стороны отправителя
    When Выбираем документ в статусе Требуется аннулирование
    When Открываем реестр Предложение об аннулировании
    Then Жмем кнопку Отклонить
    Then Ожидаем появления формы Уведомление об уточнении электронного документа
    And  Вводим причину аннулирования 123 и Подтверждаем
    Then Ожидаем всплывающее сообщения и жмем кнопку подробнее
    Then Проверяем внутри документа статус Завершен
    Then Переходим в реестр Уведомление об уточнении
    Then Переходим в режим чтения текста и видим текст 123

    Examples:
      | name |
      | ON_NSCHFDOPPR_2AE443745C8-1E68-4FBB-B893-227DED199E1D_2AEDA0511BD-14F9-493C-8F60-88D21CAB5E78_20211021_d92c4ba7-f375-4668-b4f6-ff8915a0472c.xml |
      | ON_NSCHFDOPPR_2AE443745C8-1E68-4FBB-B893-227DED199E1D_2AEDA0511BD-14F9-493C-8F60-88D21CAB5E78_20211112_241d7630-004a-4e20-abf7-946d4fe58aa8.xml |


  @YPD_ALL_DECLINE
  @fixture.browser.chrome
  Scenario Template: ДО УПД, Подписание, а после Отклонение документа
    Given Переходим на страницу тестируемого стенда
    Then Нажимаем на организацию
    Then Переходим в реестр Документы -> Черновики
    Then Произошел редирект на страницу "https://edo-2.cloud.astral-dev.ru/dcbf5864-b9cb-4ec7-801d-0e7a831b6bc2/drafts"
    When Импортируем отчет с именем "<name>"
    Then Статус документа "Отсутствует получатель"
    When Выбираем документ
    When Выбираем получателя
    Then Отправляем документ
    And Открылась форма подтверждения Подтвердить и жмем Подтвердить
    Then Проверяем статус документа "Подписывается"

    Given Переходим в реестр входящие со стороны получателя
    When Выбираем документ
    Then Статус документа "Требуется ответная подпись"
    When Подписываем документ
    Then Ожидаем всплывающее сообщение "Документ подписан"
    Then Появляется кнопка Аннулировать и документ в статусе Завершен
    Then Проверяем что появились Извещение о получении и Титул получателя
    Then Проверяем внутри документа статус Завершен

    Given Переходим в реестр входящие со стороны получателя
    When Выбираем документ
    When Нажимаем кнопку Отклонить документ
    Then Ожидаем форму Уведомление об уточнении
    And Вводим причину отклонения 123 и нажимаем Принять
    Then Статус документа Отклонен, появится реестр Уведомление об уточнении

    Examples:
      | name |
      | ON_NSCHFDOPPR_2AE443745C8-1E68-4FBB-B893-227DED199E1D_2AEDA0511BD-14F9-493C-8F60-88D21CAB5E78_20211021_d92c4ba7-f375-4668-b4f6-ff8915a0472c.xml |
      | ON_NSCHFDOPPR_2AE443745C8-1E68-4FBB-B893-227DED199E1D_2AEDA0511BD-14F9-493C-8F60-88D21CAB5E78_20211112_241d7630-004a-4e20-abf7-946d4fe58aa8.xml |

  @YPD_DECLINE
  @fixture.browser.chrome
  Scenario Template: ДО УПД, Отклонение документа
    Given Переходим на страницу тестируемого стенда
    Then Нажимаем на организацию
    Then Переходим в реестр Документы -> Черновики
    Then Произошел редирект на страницу "https://edo-2.cloud.astral-dev.ru/dcbf5864-b9cb-4ec7-801d-0e7a831b6bc2/drafts"
    When Импортируем отчет с именем "<name>"
    Then Статус документа "Отсутствует получатель"
    When Выбираем документ
    When Выбираем получателя
    Then Отправляем документ
    And Открылась форма подтверждения Подтвердить и жмем Подтвердить
    Then Проверяем статус документа "Подписывается"

    Given Переходим в реестр входящие со стороны получателя
    When Выбираем документ
    When Нажимаем кнопку Отклонить документ
    Then Ожидаем форму Уведомление об уточнении
    And Вводим причину отклонения 123 и нажимаем Принять
    Then Статус документа Отклонен, появится реестр Уведомление об уточнении

    Examples:
      | name |
      | ON_NSCHFDOPPR_2AE443745C8-1E68-4FBB-B893-227DED199E1D_2AEDA0511BD-14F9-493C-8F60-88D21CAB5E78_20211021_d92c4ba7-f375-4668-b4f6-ff8915a0472c.xml |
      | ON_NSCHFDOPPR_2AE443745C8-1E68-4FBB-B893-227DED199E1D_2AEDA0511BD-14F9-493C-8F60-88D21CAB5E78_20211112_241d7630-004a-4e20-abf7-946d4fe58aa8.xml |