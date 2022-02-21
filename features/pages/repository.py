from behave.runner import Context
from features.pages.base_page import BasePage
from features.pages.main_page import MainPage
from features.pages.auth_page import AuthPage
from features.pages.agents_page import AgentsPage
from features.pages.document_page import DocumentPage


class lazy_property:
    """Декоратор для объявления "ленивых" свойств"""

    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        value = self.func(instance)
        setattr(instance, self.func.__name__, value)
        return value


class PageRepository:
    """Репозиторий страниц"""

    def __init__(self, context: Context):
        self.context = context

    @lazy_property
    def base(self):
        return BasePage(self.context.browser)

    @lazy_property
    def main(self):
        return MainPage(self.context.browser)


    @lazy_property
    def identity(self):
        return AuthPage(self.context.browser)

    @lazy_property
    def agents(self):
        return AgentsPage(self.context.browser)

    @lazy_property
    def document(self):
        return DocumentPage(self.context.browser)

