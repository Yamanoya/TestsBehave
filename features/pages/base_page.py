import os
import time
from datetime import datetime
from typing import Tuple

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Remote as RemoteWebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from config import CONFIG, SCREENSHOTS_PATH
from features.locators.agents_page import AgentsLocators
from features.locators.auth_page import AuthPageLocators
from features.locators.document_page import DocumentPageLocators


class BasePage:
    """Базовый класс, от которого остальные классы Page наследуют общую, присущую всем функциональность"""

    # Максимальное время, за которое WebDriverWait будет ожидать событие какого-либо элемента.
    WAIT_TIMEOUT = 10

    def __init__(self, driver: RemoteWebDriver, url=CONFIG['baseUrl']):
        self.browser = driver
        self.base_url = url

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self

    def open(self):
        """Открыть базовую страницу из конфиг файла."""
        self.browser.get(self.base_url)

    def accept_alert(self):
        """Нажимает принять в аллерте"""
        try:
            WebDriverWait(self.browser, 3).until(ec.alert_is_present())
            alert = self.browser.switch_to.alert
            alert.accept()
        except TimeoutException:
            pass

    def dismiss_alert(self):
        """Нажимает отклонить в аллерте"""
        try:
            WebDriverWait(self.browser, 3).until(ec.alert_is_present())
            alert = self.browser.switch_to.alert
            alert.dismiss()
        except TimeoutException:
            pass

    def click(self, locator: Tuple[str, str]) -> None:
        """
        Кликнуть на элемент странички.
            :param locator: локатор (кортеж из типа селектора и самого селектора).
            :raise TimeoutException: возникает когда элемент в течении 10 секунд не доступен для клика
        """
        WebDriverWait(self.browser, self.WAIT_TIMEOUT).until(
            ec.element_to_be_clickable(locator)).click()

    def get_text_from_element(self, locator: Tuple[str, str]) -> str:
        """
        Получения текста из элемента по локатору
        :return: строчное значение текста из элемента
        """
        return WebDriverWait(self.browser, self.WAIT_TIMEOUT).until(
            ec.element_to_be_clickable(locator)).text

    def check_url_contains_value(self) -> bool:
        """
        Проверить наличие значения в URL.
            :param value: строчное значение того, что мы ожидаем увидеть в URL
            :return: признак наличия заданного значения в url.
        """
        try:
            WebDriverWait(self.browser, self.WAIT_TIMEOUT).until(
                ec.url_contains(CONFIG["baseUrl"]))
            return True
        except TimeoutException:
            return False

    def check_number_of_browser_tabs(self, count: int) -> bool:
        """
        Проверить наличие заданного количества вкладок браузера.
            :param count: ожидаемое количество вкладок браузера.
            :return: признак совпадения фактического количества вкладок с ожидаемым.
        """
        try:
            WebDriverWait(self.browser, self.WAIT_TIMEOUT).until(
                ec.number_of_windows_to_be(count))
            return True
        except TimeoutException:
            return False

    def switch_to_browser_tab(self, number: int) -> None:
        """
        Переключится на вкладку браузера.
            :param number: номер вкладки (начиная с 1-го) на которую нужно переключится.
        """
        tab_name = self.browser.window_handles[number - 1]
        self.browser.switch_to.window(tab_name)

    def close_browser_tab(self, number: int):
        """
        Закрыть вкладку.
            :param number: Номер вкладки (начиная с 1-го) которую нужно закрыть.
        """
        tab_name = self.browser.window_handles[number - 1]
        self.browser.switch_to.window(tab_name)
        self.browser.close()

    def check_an_element_is_present(self, locator: Tuple[str, str], timeout=10):
        """
        Проверка на то, что элемент присутствует на странице.
            :param locator: локатор для нахождения элемента на странице
            :param timeout: время, за которое WebDriverWait будет ожидать событие
            :return: признак, что элемент НЕ был найден на странице.
        """
        try:
            WebDriverWait(self.browser, timeout).until(
                ec.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def check_an_element_is_not_present(self, locator: Tuple[str, str], timeout=0.5) -> bool:
        """
        Проверить, что элемент не появляется на странице в течение заданного времени.
        Появился - упал. Не появился - зеленый.
            :param locator: локатор для нахождения элемента на странице
            :param timeout: время, за которое WebDriverWait будет ожидать событие (в данном случае - НЕ появление элемента в DOM)
            :return: признак, что элемент НЕ был найден на странице.
        """
        try:
            WebDriverWait(self.browser, timeout).until(
                ec.presence_of_element_located(locator))
            return False
        except TimeoutException:
            return True

    def check_an_element_is_disappear(self, locator: Tuple[str, str], timeout=4) -> bool:
        """
        Проверить, что элемент исчезнет. Будет ждать пока элемент не исчезнет.
            :param locator: локатор для нахождения элемента на странице
            :param timeout: время, за которое WebDriverWait будет ожидать событие (в данном случае - НЕ появление элемента в DOM)
            :return: признак, что элемент исчез со страницы.
        """
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                ec.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False


    def check_text_is_not_empty(self, locator: Tuple[str, str], timeout=4, ) -> bool:
        """
        Проверяет элемент, если тот не пустой(есть внутри строчное значение), возвращает True.
        """
        if WebDriverWait(self.browser, timeout).until(
                ec.presence_of_element_located(locator)).text != '':
            return True
        else:
            return False

    def get_quantity_of_elements(self, locator: Tuple[str, str]) -> int:
        """Возвращает количество элементов по локатору"""
        try:
            return len(WebDriverWait(self.browser, self.WAIT_TIMEOUT).until(
                ec.visibility_of_all_elements_located(locator)))
        except TimeoutException:
            return 0

    def create_screenshot(self, screenshot_name: str):
        """
        Делает скриншот и сохраняет в директорию которая указана в конфиге
        Добавлена доп логика, если директория отсктствует, он ее создаст
        """
        # sleep добавлен из-за непредсказуемости отображения печати.
        time.sleep(3)
        self.browser.save_screenshot(os.path.join(SCREENSHOTS_PATH, f"{screenshot_name}.png"))

    def input_in_search(self, value: str) -> None:
        """
        Ввод в поле поиска значения по которому будет проходить поиск (ТОЛЬКО ВВОД, НЕ НАЖИМАЕТ НА "ПОИСК")
            :param value: значение по которому мы ищем видео.
            :raise TimeoutException: возникает, когда отчет не удалось найти по заданному имени.
        """
        WebDriverWait(self.browser, self.WAIT_TIMEOUT).until(
            ec.visibility_of_element_located(AuthPageLocators.FIELD_EMAIL)).send_keys(value)

    def input_in_password(self, value: str) -> None:
        """
        Ввод в поле поиска значения по которому будет проходить поиск (ТОЛЬКО ВВОД, НЕ НАЖИМАЕТ НА "ПОИСК")
            :param value: значение по которому мы ищем видео.
            :raise TimeoutException: возникает, когда отчет не удалось найти по заданному имени.
        """
        WebDriverWait(self.browser, self.WAIT_TIMEOUT).until(
            ec.visibility_of_element_located(AuthPageLocators.FIELD_PASSWORD)).send_keys(value)


    def input_for_search_agent(self) -> None:
        """
        Ввод в поле поиска значения по которому будет проходить поиск (ТОЛЬКО ВВОД, НЕ НАЖИМАЕТ НА "ПОИСК")
            :param value: значение по которому мы ищем видео.
            :raise TimeoutException: возникает, когда отчет не удалось найти по заданному имени.
        """
        WebDriverWait(self.browser, self.WAIT_TIMEOUT).until(
            ec.visibility_of_element_located(AgentsLocators.MY_AGENTS_FIELD_SEARCH)).send_keys(CONFIG["ID_2"])


    def input_for_search_agent_with_value(self, value: str) -> None:
        """
        Ввод в поле поиска значения по которому будет проходить поиск (ТОЛЬКО ВВОД, НЕ НАЖИМАЕТ НА "ПОИСК")
            :param value: значение по которому мы ищем видео.
            :raise TimeoutException: возникает, когда отчет не удалось найти по заданному имени.
        """
        WebDriverWait(self.browser, self.WAIT_TIMEOUT).until(
            ec.visibility_of_element_located(AgentsLocators.MY_AGENTS_FIELD_SEARCH)).send_keys(value)


    def search_all_inn(self, first_value: str) -> None:
        """
        Ввод в поле поиска значения по которому будет проходить поиск (ТОЛЬКО ВВОД, НЕ НАЖИМАЕТ НА "ПОИСК")
            :param value: значение по которому мы ищем видео.
            :raise TimeoutException: возникает, когда отчет не удалось найти по заданному имени.
        """
        WebDriverWait(self.browser, self.WAIT_TIMEOUT).until(
            ec.visibility_of_element_located(AgentsLocators.INN_SEARCH_ALL)).send_keys(first_value)

    def search_all_kpp(self, second_value: str) -> None:
        """
        Ввод в поле поиска значения по которому будет проходить поиск (ТОЛЬКО ВВОД, НЕ НАЖИМАЕТ НА "ПОИСК")
            :param value: значение по которому мы ищем видео.
            :raise TimeoutException: возникает, когда отчет не удалось найти по заданному имени.
        """
        WebDriverWait(self.browser, self.WAIT_TIMEOUT).until(
            ec.visibility_of_element_located(AgentsLocators.KPP_SEARCH_ALL)).send_keys(second_value)


    def import_file(self, path_to_file: str):
        """
        Импортировать файл.
            :param path_to_file: Путь до файла кторый мы импортируем.
        """
        self.browser.find_element(*DocumentPageLocators.IMPORT_FILE).send_keys(path_to_file)




