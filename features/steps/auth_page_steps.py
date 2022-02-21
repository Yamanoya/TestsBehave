import time

from behave import *
from behave.runner import Context


@Given('Открываем страницу авторизации и авторизируемся')
def authorization(ctx: Context):
    """Авторизация"""
    ctx.pages.identity.open()
    ctx.pages.identity.authorization_by_email()
    time.sleep(1)  # ждем чуть-чуть, чтобы главная прогрузилась



