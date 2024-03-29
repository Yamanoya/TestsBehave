import time
from behave import fixture, use_fixture
from behave.model import Scenario, Tag
from behave.runner import Context
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from features.pages.repository import PageRepository
from behave.model import Step
import config
from allure_behave.hooks import allure_report


def browser_chrome(context: Context):
    options = webdriver.ChromeOptions()
    options.add_argument('no-sandbox')
    options.add_argument('disable-extensions')
    options.add_argument('start-maximized')

    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    context.browser = browser
    yield context.browser
    context.browser.quit()


def browser_firefox(context: Context):
    # Аналог метода для хрома browser_chrome
    # Обявляем экземпляр класа фаерфокс GeckoDriverManager класс для автоматического скачивания драйвера.
    browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    context.browser = browser
    yield context.browser
    context.browser.quit()


# Словарь который используется для подготовки фикстур before_tag,
# в значениях прописаны имена функций в которых создаются экземпляры класа браузер
fixture_registry = {
    "fixture.browser.firefox": browser_firefox,
    "fixture.browser.chrome": browser_chrome
}


def before_tag(context: Context, tag: Tag):
    """Подготовка фикстур. Для запуска сценариев в разных браузерах"""
    if tag.startswith("fixture."):
        return use_fixture(fixture_registry.get(tag), context)


def before_scenario(ctx: Context, scenario: Scenario):
    """Авторизация на тестовом стенде перед запуском тестового сценария."""
    ctx.pages = PageRepository(ctx)

    if scenario.feature.name == "Проверка страницы авторизации":
        return
    ctx.pages.identity.open()
    ctx.pages.identity.authorization_by_email()
    assert ctx.pages.main.url_is_main()


def after_step(ctx: Context, step: Step):
    """
    При падении шага создает скриншот
    """
    if step.status == 'failed':
        step_name = step.filename.replace("features/", "") + "." + str(step.line)
        ctx.pages.base.create_screenshot(step_name)
