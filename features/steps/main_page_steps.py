from behave import *
from behave.runner import Context
from config import CONFIG


@Given('Открыта форма авторизации')
def main_page_is_open(ctx: Context):
    """Проверка по урлу, что мы находимся на главной странице"""
    ctx.pages.base.open()
    # assert ctx.pages.main.url_is_main()


@Given('Переходим на страницу тестируемого стенда')
def check_url(ctx: Context):
    """
    Проверяет не полный урл, а наличие значения внутри урла страницы
    """
    assert ctx.pages.base.check_url_contains_value()









