import time
from behave import *
from behave.runner import Context

from features.locators.agents_page import AgentsLocators
from features.locators.document_page import DocumentPageLocators
from features.pages.agents_page import AgentsPage


@Given('Открыт реестр Мои контрагенты')
def given_incoming_page(context):
    AgentsPage(context.browser).open_agents()
    time.sleep(1)

@Then('Нажимаем на реестр Контрагенты')
def click_at_agents(ctx: Context):
    """Нажать на реестр Контрагенты"""
    ctx.pages.base.click(AgentsLocators.AGENTS_LIST)


@Then('Нажимаем на реестр Мои Контрагенты')
def click_at_my_agents(ctx: Context):
    """Нажать на реестр Мои Контрагенты"""
    ctx.pages.base.click(AgentsLocators.MY_AGENTS_LIST)


@When('Нажимаем на кнопку Добавить контрагента')
def click_at_button_add_agent(ctx: Context):
    """Нажать на кнопку Добавить контрагента"""
    ctx.pages.base.click(AgentsLocators.ADD_MY_AGENT_BUTTON)
    time.sleep(3)


#@When('Проверка кол-ва контрагентов {value}')
#def check_value_agents_in_my_agents(ctx: Context, value: str):
   # name = ctx.pages.base.get_text_from_element(AgentsLocators.MY_AGENTS_VALUE)
   # assert name == value, f'Кол-во агентов "{name}", ожидалось "{value}"'


@Then('Проверяем что открылась форма Добавление контрагента')
def check_value(ctx: Context):
    ctx.pages.base.check_an_element_is_present(AgentsLocators.FORM_ADD_AGENT)
    time.sleep(2)


@When('Вводим в поле ID контрагента {value}')
def input_for_search_agent(ctx: Context, value: str):
    """Нажать на кнопку "Войти" в шапке сайта"""
    ctx.pages.base.input_for_search_agent(value)
    time.sleep(2)


@Then('Проверяем найденого контрагента {name_agent}')
def check_value(ctx: Context, name_agent: str):
    name = ctx.pages.base.get_text_from_element(AgentsLocators.NAME_AGENT)
    assert name == name_agent, f'Наименование формы "{name}", ожидалось "{name_agent}"'


@Then('Отправляем приглашение контрагенту')
def send_invite_for_agent(ctx: Context):
    """Жмем кнопку отправить приглашение контрагенту"""
    ctx.pages.base.click(AgentsLocators.MY_AGENTS_SEND_INVITE_AGENT)


@When('Нажимаем на всплывающее сообщение')
def click_at_sms(ctx: Context):
    ctx.pages.base.click(AgentsLocators.MY_AGENTS_REFRESH_LIST_BUTTON)
    time.sleep(3)



@Then('Нажимаем на всплывающее сообщение')
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


@When('Проверка кол-ва контрагентов в Моих контрагентах {value_my_agents}')
def check_value_my_agents(ctx: Context, value_my_agents: str):
    name = ctx.pages.base.get_text_from_element(AgentsLocators.VALUE_AGENTS_AT_MY_AGENTS)
    assert name == value_my_agents, f'Кол-во агентов "{name}", ожидалось "{value_my_agents}"'


@Then('Проверка имени контрагента {value_name_agent}')
def check_agent(ctx: Context, value_name_agent: str):
    name = ctx.pages.base.get_text_from_element(AgentsLocators.NAME_AGENT)
    assert name == value_name_agent, f'Кол-во агентов "{name}", ожидалось "{value_name_agent}"'

@When('Нажимаем на организацию')
def click(ctx: Context):
    """Нажать на Выбрать организацю"""
    ctx.pages.base.click(DocumentPageLocators.TAKE_ORGANIZATION)
    time.sleep(1)

@When('Наводим на элемент')
def mouse_over(ctx: Context):
    ctx.pages.agents.mouse_over()


@When("Нажимаем на кнопку Принять")
def click_at_accept(ctx: Context):
    ctx.pages.base.click(AgentsLocators.INVITE_ACCEPT_BUTTON)


@Then("Наводим на элемент КПП")
def mouse_over_kpp(ctx: Context):
    ctx.pages.agents.mouse_over_kpp()

@Then("Нажимаем кнопку удалить")
def delete_agent(ctx: Context):
    ctx.pages.base.click(AgentsLocators.DELETE_AGENT)