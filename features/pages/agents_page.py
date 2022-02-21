import os
from datetime import datetime
import time
from typing import List, Tuple
from selenium.webdriver import Remote as RemoteWebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from config import CONFIG, SCREENSHOTS_PATH
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from features.pages.base_page import BasePage
from urllib.parse import urljoin


class AgentsPage(BasePage):
    def mouse_over(self):
        target = self.browser.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/main[1]/div[1]/ul[1]/li[1]/div[1]/div[5]")

        action = ActionChains(self.browser)
        action.move_to_element(target).perform()


    def mouse_over_kpp(self):
        target_kpp = self.browser.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/main[1]/div[1]/ul[1]/li[1]/a[1]/div[3]")

        action = ActionChains(self.browser)
        action.move_to_element(target_kpp).perform()


    def open_agents(self):
        """Открыть реестр Входящие"""
        self.browser.get(urljoin(self.base_url, '/8be142a1-5b65-4fd8-b56a-e6ad69d7d1ae/documents/incoming'))
