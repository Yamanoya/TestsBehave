from urllib.parse import urljoin
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from features.pages.base_page import BasePage
from features.locators.document_page import DocumentPageLocators
from config import CONFIG


class DocumentPage(BasePage):

    def open_incoming(self):
        """Открыть реестр Входящие у получателя"""
        self.browser.get(urljoin(self.base_url, CONFIG["INCOMING"]))

    def open_incoming_sender(self):
        """Открыть реестр Исходящие у отправителя"""
        self.browser.get(urljoin(self.base_url, CONFIG["OUTGOING"]))

    def open_draft(self):
        """Открыть реестр Черновики у отправителя"""
        self.browser.get(
            urljoin(self.base_url, CONFIG["DRAFT"]))

    def input_value_in_field_cancel(self, value: str) -> None:
        WebDriverWait(self.browser, self.WAIT_TIMEOUT).until(
            ec.visibility_of_element_located(DocumentPageLocators.FIELD_ACCEPT_CANCEL)).send_keys(value)

    def input_text_in_field_cancel(self, value: str) -> None:
        WebDriverWait(self.browser, self.WAIT_TIMEOUT).until(
            ec.visibility_of_element_located(DocumentPageLocators.FIELD_FOR_ADD_TEXT)).send_keys(value)






