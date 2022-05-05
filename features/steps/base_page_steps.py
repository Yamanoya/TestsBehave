import time


from behave import *
from behave.runner import Context

from features.locators.auth_page import AuthPageLocators


@When('Нажимаем на кнопку Email')
def click_at_sign(ctx: Context):
    """Нажать на поле Email"""
    ctx.pages.base.click(AuthPageLocators.SWITCH_ON_EMAIL)
    time.sleep(1)


@Then('Выбираем поле password и вводим пароль "{value}"')
def input_in_password(ctx: Context, value: str):
    """Нажать на кнопку "Войти" в шапке сайта"""
    ctx.pages.base.input_in_password(value)


@Then('Вводим в поле поиска значение "{value}"')
def input_in_search(ctx: Context, value: str):
    ctx.pages.base.input_in_search(value)


@When('Нажимаем "Войти"')
def click_do_search(ctx: Context):
    """
    Кнопка поиск не всегда нажимается без явного ожидания,
    хотя стоит условие element_to_be_clickable в чем проблема - хз, нужно дебажить, нет времени.
    """
    time.sleep(2)
    ctx.pages.base.click(AuthPageLocators.ENTER_BUTTON)




