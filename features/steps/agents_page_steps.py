import time
from behave import *
from behave.runner import Context

from features.locators.agents_page import AgentsLocators
from features.pages.agents_page import AgentsPage


@Given('Открываем реестр Мои контрагенты')
def given_incoming_page(context):
    AgentsPage(context.browser).open_agents()
    time.sleep(1)

@Then('Попадаем на страницу организаций')
def open_all_organization(ctx: Context):
    ctx.pages.base.check_an_element_is_present(AgentsLocators.MAIN_PAGE)

@Then('Открывается карточка организации')
def open_card_organization(ctx: Context):
    ctx.pages.base.check_an_element_is_present(AgentsLocators.ORGANIZ_CARD)

@Then('Переходим в реестр Контрагенты -> Мои контрагенты')
def click_at_agents(ctx: Context):
    ctx.pages.base.click(AgentsLocators.AGENTS_LIST)
    ctx.pages.base.check_an_element_is_present(AgentsLocators.MY_AGENTS_LIST)
    ctx.pages.base.click(AgentsLocators.MY_AGENTS_LIST)
    ctx.pages.base.check_an_element_is_present(AgentsLocators.ADD_MY_AGENT_BUTTON)
    ctx.pages.base.click(AgentsLocators.ADD_MY_AGENT_BUTTON)



@Then('Проверяем что открылась форма Добавление контрагента')
def check_value(ctx: Context):
    ctx.pages.base.check_an_element_is_present(AgentsLocators.FORM_ADD_AGENT)
    time.sleep(2)


@Then('Добавляем контрагента с ID {value}')
def input_for_search_agent_with_value(ctx: Context, value: str):
    """Нажать на кнопку "Войти" в шапке сайта"""
    ctx.pages.base.input_for_search_agent_with_value(value)
    time.sleep(2)

@Then('Добавляем контрагента')
def add_agent(ctx: Context):
    ctx.pages.base.input_for_search_agent()


@Then('Проверяем найденого контрагента {name_agent}')
def check_value(ctx: Context, name_agent: str):
    name = ctx.pages.base.get_text_from_element(AgentsLocators.NAME_AGENT)
    assert name == name_agent, f'Наименование формы "{name}", ожидалось "{name_agent}"'


@Then('Отправляем приглашение контрагенту')
def send_invite_for_agent(ctx: Context):
    """Жмем кнопку отправить приглашение контрагенту"""
    ctx.pages.base.click(AgentsLocators.MY_AGENTS_SEND_INVITE_AGENT)

@Then('Попадаем на организацию Получателя приглашения, в реестр Контрагенты -> Приглашения')
def check_register(ctx: Context):
    ctx.pages.base.check_an_element_is_present(AgentsLocators.NAME_AGENT)

@When('Нажимаем на всплывающее сообщение')
def click_at_sms(ctx: Context):
    ctx.pages.base.click(AgentsLocators.MY_AGENTS_REFRESH_LIST_BUTTON)
    time.sleep(3)

@When('Нажимаем Обновить список и перейти к приглашениям во всплывающем сообщении')
def click_at_sms_about(ctx: Context):
    ctx.pages.base.click(AgentsLocators.MY_AGENTS_REFRESH_LIST_BUTTON_ABOUT)


@Then('Проверка кол-ва контрагентов в Приглашениях {value_invite}')
def check_value_agents(ctx: Context, value_invite: str):
    name = ctx.pages.base.get_text_from_element(AgentsLocators.INVITE_INPUT_INVITATION)
    assert name == value_invite, f'Кол-во агентов "{name}", ожидалось "{value_invite}"'
    time.sleep(2)


@Then('Нажимаем на чек бокс')
def click_at_checkbox(ctx: Context):
    """Нажать на кнопку Добавить контрагента"""
    ctx.pages.base.click(AgentsLocators.INVITE_CHECKBOX_BUTTON)



@Then('Принимаем контрагента')
def click_at_checkbox(ctx: Context):
    """Нажать на кнопку Добавить контрагента"""
    ctx.pages.base.click(AgentsLocators.INVITE_ACCEPT_BUTTON)


@Then('Кол-во контрагентов в Моих контрагентах становится равным {value_my_agents}')
def check_value_my_agents(ctx: Context, value_my_agents: str):
    name = ctx.pages.base.get_text_from_element(AgentsLocators.VALUE_AGENTS_AT_MY_AGENTS)
    assert name == value_my_agents, f'Кол-во агентов "{name}", ожидалось "{value_my_agents}"'


@Then('Имя контрагента {value_name_agent}')
def check_agent(ctx: Context, value_name_agent: str):
    name = ctx.pages.base.get_text_from_element(AgentsLocators.NAME_AGENT)
    assert name == value_name_agent, f'Кол-во агентов "{name}", ожидалось "{value_name_agent}"'

@When('Выбираем организацию')
def click(ctx: Context):
    """Нажать на Выбрать организацю"""
    ctx.pages.base.click(AgentsLocators.TAKE_ORGANIZATION)
    time.sleep(1)

@Then('Принимаем приглашение')
def mouse_over(ctx: Context):
    ctx.pages.agents.mouse_over()
    time.sleep(2)
    ctx.pages.base.click(AgentsLocators.INVITE_ACCEPT_BUTTON)


@Then("Выбираем запись")
def mouse_over_kpp(ctx: Context):
    ctx.pages.agents.mouse_over_kpp()

@Then("Удаляем запись")
def delete_agent(ctx: Context):
    ctx.pages.base.click(AgentsLocators.DELETE_AGENT)


@Then("Текст Возможно, вы ввели ID ЭДО не полностью")
def check_text(ctx: Context):
    ctx.pages.base.check_an_element_is_present(AgentsLocators.SEARCH_ALL, timeout=10)

@Then("Нажать кнопку Расширенный поиск")
def click_search(ctx: Context):
    ctx.pages.base.click(AgentsLocators.SEARCH_ALL)

@Then("На форме поиска контрагента по ИНН и КПП, вводим данные ИНН - {first_value} КПП {second_value}")
def input_inn_kpp(ctx: Context, first_value: str, second_value: str):
    ctx.pages.base.click(AgentsLocators.INN_SEARCH_ALL)
    ctx.pages.base.search_all_inn(first_value)
    time.sleep(1)
    ctx.pages.base.click(AgentsLocators.KPP_SEARCH_ALL)
    ctx.pages.base.search_all_kpp(second_value)
    ctx.pages.base.click(AgentsLocators.FIND_BUTTON)



