Feature: Проверка добавления контрагента

  @all
  @add_agent
  @fail_search
  @fixture.browser.chrome
  Scenario: Поиск контрагента, с неверными данными
    Given Переходим на страницу тестируемого стенда
    Then Попадаем на страницу организаций
    When Выбираем организацию
    Then Открывается карточка организации
    Then Переходим в реестр Контрагенты -> Мои контрагенты
    And  Добавляем контрагента с ID 2AE8BE142A1-5B65-4FD8-B56A-E6AD69D7D1A
    Then Текст Возможно, вы ввели ID ЭДО не полностью
    And  Нажать кнопку Расширенный поиск
    Then На форме поиска контрагента по ИНН и КПП, вводим данные ИНН - 9681291515 КПП 999999999


  @add_agent
  @fixture.browser.chrome
  Scenario: Добавление контрагента
    Given Переходим на страницу тестируемого стенда
    Then Попадаем на страницу организаций
    When Выбираем организацию
    Then Открывается карточка организации
    Then Переходим в реестр Контрагенты -> Мои контрагенты
    And  Добавляем контрагента
    And  Отправляем приглашение контрагенту
    When Нажимаем Обновить список и перейти к приглашениям во всплывающем сообщении
    Then Попадаем на организацию Получателя приглашения, в реестр Контрагенты -> Приглашения
    And  Принимаем приглашение
    Then Появляется всплывающее сообщение
    When Нажимаем Обновить список и перейти к приглашениям во всплывающем сообщении
    Then Кол-во контрагентов в Моих контрагентах становится равным 1
    And  Имя контрагента _ТестВоркЮЛ_


    # Удаление контрагента
  @all
  @delete_agent
  @fixture.browser.chrome
  Scenario: Удаление контрагента
    Given Открываем реестр Мои контрагенты
    When Выбираем организацию
    Then Переходим в реестр Контрагенты -> Мои контрагенты
    Then Выбираем запись
    And Удаляем запись



