from config import CONFIG
from features.pages.base_page import BasePage
from features.locators.auth_page import AuthPageLocators


class AuthPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(AuthPage, self).__init__(*args, **kwargs)

    def open(self):
        """Открыть страницу."""
        self.browser.get(self.base_url)
        self.browser.add_cookie({"name": "recaptcha", "value": "disabled"})

    def authorization_by_email(self):
        """Авторизация по почте и паролю"""
        auth_toggle = self.browser.find_element(*AuthPageLocators.SWITCH_ON_EMAIL)
        auth_toggle.click()
        email_field = self.browser.find_element(*AuthPageLocators.FIELD_EMAIL)
        email_field.send_keys(CONFIG["mail"])
        password_field1 = self.browser.find_element(*AuthPageLocators.FIELD_PASSWORD)
        password_field1.send_keys(CONFIG["password"])
        self.click(AuthPageLocators.ENTER_BUTTON)
