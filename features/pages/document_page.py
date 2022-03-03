from urllib.parse import urljoin
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from features.pages.base_page import BasePage
from features.locators.document_page import DocumentPageLocators

class DocumentPage(BasePage):

    def open_incoming(self):
        """Открыть реестр Входящие у получателя"""
        self.browser.get(urljoin(self.base_url, '/82aecc39-0c5e-4f9f-b2d2-59f84e3ff5a8/documents/incoming'))

    def open_incoming_sender(self):
        """Открыть реестр Исходящие у отправителя"""
        self.browser.get(urljoin(self.base_url, '/0222550a-29d8-4647-94f2-a1f6e34230e0/documents/outgoing'))

    def input_value_in_field_cancel(self, value: str) -> None:
        WebDriverWait(self.browser, self.WAIT_TIMEOUT).until(
            ec.visibility_of_element_located(DocumentPageLocators.FIELD_ACCEPT_CANCEL)).send_keys(value)

    def input_text_in_field_cancel(self, value: str) -> None:
        WebDriverWait(self.browser, self.WAIT_TIMEOUT).until(
            ec.visibility_of_element_located(DocumentPageLocators.FIELD_FOR_ADD_TEXT)).send_keys(value)