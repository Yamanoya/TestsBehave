import os
import time

from config import REPORTS_FOR_IMPORT_PATH

from behave import *
from behave.runner import Context

from features.locators.document_page import DocumentPageLocators
from features.pages.document_page import DocumentPage


@Given('Открыт реестр Входящих документов у получателя')
def given_incoming_page(context):
    DocumentPage(context.browser).open_incoming()
    time.sleep(1)

@Given('Открыт реестр Исходящих документов со стороны отправителя')
def given_incoming_page(context):
    DocumentPage(context.browser).open_incoming_sender()
    time.sleep(1)

@Given ('Открыт реестр Черновики')
def open_draft(context):
    DocumentPage(context.browser).open_draft()
    time.sleep(1)

@When('Импортируем отчет с именем "{name}"')
def import_file(ctx: Context, name: str):
    """Импорт документа для дальнейшей работы с ним"""
    ctx.pages.base.import_file(os.path.join(REPORTS_FOR_IMPORT_PATH, name))
    time.sleep(1)


@Then('Нажимаем на реестр Документы')
def click_at_sign(ctx: Context):
    """Нажать на реестр Документы"""
    ctx.pages.base.click(DocumentPageLocators.RES_DOCUMENTS)


@Then('Нажимаем на Черновики')
def click_at_sign(ctx: Context):
    """Нажать на реестр Черновики"""
    ctx.pages.base.click(DocumentPageLocators.RES_CHER)
    time.sleep(2)


@Then('Нажимаем на организацию')
def click(ctx: Context):
    """Нажать на Выбрать организацю"""
    ctx.pages.base.click(DocumentPageLocators.TAKE_ORGANIZATION)
    time.sleep(2)


@Then('Статус документа "{name_status}"')
def check_quantity_sign_in_button(ctx: Context, name_status: str):
    first_video_name = ctx.pages.base.get_text_from_element(DocumentPageLocators.STATUS_DOCUMENT)
    assert first_video_name == name_status, f'Статус документа "{first_video_name}", ожидалось "{name_status}"'


@Then('Проверка имени файла "{name_document}"')
def check_quantity_sign_in_button(ctx: Context, name_document: str):
    name = ctx.pages.base.get_text_from_element(DocumentPageLocators.NAME_DOCUMENT_AFTER_ADD)
    assert name == name_document, f'Статус документа "{name}", ожидалось "{name_document}"'
    time.sleep(1)


@Then('Кликаем по документу')
def click_at_sign(ctx: Context):
    """Нажать на реестр Документы"""
    ctx.pages.base.click(DocumentPageLocators.DOCUMENT_ADD_LOCATOR)
    time.sleep(1)


@Then('Проверяем имя документа "{name_document}"')
def check_quantity_sign_in_button(ctx: Context, name_document: str):
    name = ctx.pages.base.get_text_from_element(DocumentPageLocators.NAME_DOCUMENT)
    assert name == name_document, f'Имя документа "{name}", ожидалось "{name_document}"'


@When('Нажимаем на кнопку Выбрать получателя')
def click_at_sending(ctx: Context):
    """Нажать на кнопку Выбрать получателя"""
    ctx.pages.base.click(DocumentPageLocators.TAKE_SENDING)
    time.sleep(1)


@Then('Проверяем присутствие получателя "{name_document}"')
def check_quantity_sign_in_button(ctx: Context, name_document: str):
    name = ctx.pages.base.get_text_from_element(DocumentPageLocators.NAME_DOCUMENT)
    assert name == name_document, f'Статус документа "{name}", ожидалось "{name_document}"'


@Then('Выбираем контрагента')
def click_at_sendig_document(ctx: Context):
    """Нажать на кнопку Выбрать получателя"""
    ctx.pages.base.click(DocumentPageLocators.TAKE_AGENT)
    time.sleep(2)


@When('Закрываем форму')
def click_at_clear_field(ctx: Context):
    """Нажать на пустое поле"""
    ctx.pages.base.click(DocumentPageLocators.CLOSE_BUTTON)
    time.sleep(1)

@Then('Нажимаем кнопку отправить')
def click_at_clear_field(ctx: Context):
    """Нажать на пустое поле"""
    ctx.pages.base.click(DocumentPageLocators.SEND_BUTTON)


@Then('Проверяем что открылась форма подтверждения {check_button} и жмем Подтвердить')
def check_open_form_and_click_at_button(ctx: Context, check_button: str):
    """Проверяем что открылась форма подтверждения и жмем Подтвердить"""
    name = ctx.pages.base.get_text_from_element(DocumentPageLocators.ACCEPT_BUTTON)
    assert name == check_button, f'Имя кнопки "{name}", ожидалось "{check_button}"'
    ctx.pages.base.click(DocumentPageLocators.ACCEPT_BUTTON)


@Then('Проверяем кол-во выбранных агентов "{take_agent}"')
def check_quantity_all_take_agents(ctx: Context, take_agent: str):
    name = ctx.pages.base.get_text_from_element(DocumentPageLocators.TAKE_ALL_AGENTS)
    assert name == take_agent, f'Кол-во выбранных "{name}", ожидалось "{take_agent}"'


@Then('Документ в статусе "{status_document}"')
def check_quantity_all_take_agents(ctx: Context, status_document: str):
    name = ctx.pages.base.get_text_from_element(DocumentPageLocators.STATUS_SIGNATURE)
    assert name == status_document, f'Статус документа "{name}", ожидалось "{status_document}"'


@Then('Проверяем что документ в статусе {value_status}')
def check_at_status_value(ctx: Context, value_status: str):
    ctx.pages.base.check_an_element_is_present(DocumentPageLocators.STATUS_WAIT_SIGNATURE, timeout=20)
    name = ctx.pages.base.get_text_from_element(DocumentPageLocators.STATUS_WAIT_SIGNATURE)
    assert name == value_status, f'Должно быть входящий докумет "{name}", ожидалось "{value_status}"'


@Then('Ждем алерт и жмем кнопку')
def wait_alert_and_click(ctx: Context):
    ctx.pages.base.check_an_element_is_present(DocumentPageLocators.INCOMING_DOCUMENT, timeout=30)
    ctx.pages.base.click(DocumentPageLocators.INCOMING_DOCUMENT)


@When('Выбираем документ')
def take_document(ctx: Context):
    ctx.pages.base.click(DocumentPageLocators.DOCUMENT_INCOMING)


@Then('Проверяем что документ внутри в статусе {value_status}')
def check_at_status_value(ctx: Context, value_status: str):
    name = ctx.pages.base.get_text_from_element(DocumentPageLocators.STATUS_WAIT_SIGNATURE_IN_DOCUMENT)
    assert name == value_status, f'Должно быть входящий докумет "{name}", ожидалось "{value_status}"'


@When('Нажимаем подписать документ')
def take_document(ctx: Context):
    ctx.pages.base.click(DocumentPageLocators.SIGN_A_DOCUMENT)


@Then('Ожидаем всплывающее сообщение')
def wait_alert_about_click_take_document(ctx: Context):
    ctx.pages.base.check_an_element_is_present(DocumentPageLocators.SIGN_DOCUMENT_MESSAGE, timeout=30)


@Then('Появляется кнопка Аннулировать и документ в статусе {status_check}')
def check_button_decline(ctx: Context, status_check: str):
    name = ctx.pages.base.get_text_from_element(DocumentPageLocators.END_DOCUMENT)
    assert name == status_check, f'Должно быть входящий докумет "{name}", ожидалось "{status_check}"'

@Then('Проверяем что появились {value_one} и {value_two}')
def check_registry(ctx: Context, value_one: str, value_two: str):
    name = ctx.pages.base.get_text_from_element(DocumentPageLocators.REGISTRY_RECEIPT_NOTICE)
    assert name == value_one, f'Должно быть "{name}", ожидалось "{value_one}"'
    name_two = ctx.pages.base.get_text_from_element(DocumentPageLocators.REGISTRY_BENEFICIARY_TITLE)
    assert name_two == value_two, f'Должно быть "{name}", ожидалось "{value_two}"'

@Then('Проверяем что появилось {value_one}')
def check_registry(ctx: Context, value_one: str):
    name = ctx.pages.base.get_text_from_element(DocumentPageLocators.REGISTRY_RECEIPT_NOTICE)
    assert name == value_one, f'Должно быть "{name}", ожидалось "{value_one}"'

@Then('Проверяем внутри документа статус {value_status}')
def check_at_status_value(ctx: Context, value_status: str):
    ctx.pages.base.check_an_element_is_present(DocumentPageLocators.END_DOCUMENT)
    name = ctx.pages.base.get_text_from_element(DocumentPageLocators.END_DOCUMENT)
    assert name == value_status, f'Должно быть входящий докумет "{name}", ожидалось "{value_status}"'

@When ('Нажимаем на кнопку Аннулировать документ')
def click_at_cancel_document(ctx: Context):
    ctx.pages.base.click(DocumentPageLocators.DECLINE_BUTTON)

@Then('Откроется форма {value}')
def check_at_open_form(ctx: Context, value: str):
    name = ctx.pages.base.get_text_from_element(DocumentPageLocators.FORM_FOR_ACCEPT_CANCEL)
    assert name == value, f'Должно быть "{name}", ожидалось "{value}"'

@Then('Вводим причину аннулирования {value} и нажимаем Принять')
def click_at_field_and_write_text(ctx: Context, value: str):
    ctx.pages.base.check_an_element_is_present(DocumentPageLocators.FIELD_ACCEPT_CANCEL, timeout=10)
    ctx.pages.document.input_value_in_field_cancel(value)
    time.sleep(1)
    ctx.pages.base.click(DocumentPageLocators.BUTTON_ACCEPT_CANCEL)

@Then('Ожидаем всплывающее сообщение об аннуровании и нажимаем подробнее')
def wait_form_about_cancel_and_click_more(ctx: Context):
    ctx.pages.base.check_an_element_is_present(DocumentPageLocators.MESSAGE_ABOUT_CANCEL, timeout=30)
    ctx.pages.base.click(DocumentPageLocators.MESSAGE_ABOUT_CANCEL)

@Then('Проверяем наличие текста {value}')
def check_at_open_form(ctx: Context, value: str):
    name = ctx.pages.base.get_text_from_element(DocumentPageLocators.STATUS_NEED_CANCEL)
    assert name == value, f'Должно быть "{name}", ожидалось "{value}"'

@Then('Проверяем что находимся в реестре {value}')
def check_at_open_form(ctx: Context, value: str):
    name = ctx.pages.base.get_text_from_element(DocumentPageLocators.REGISTER_CANCEL_INGOING)
    assert name == value, f'Должно быть "{name}", ожидалось "{value}"'

@Then('Нажимаем Принять аннулирование')
def click_at_cancel(ctx: Context):
    ctx.pages.base.check_an_element_is_present(DocumentPageLocators.BUTTON_ACCEPT_CANCEL_IN_DOCUMENT, timeout=30)
    ctx.pages.base.click(DocumentPageLocators.BUTTON_ACCEPT_CANCEL_IN_DOCUMENT)

@Then('Аннулирование одобрено')
def check_cancel_is_okay(ctx: Context):
    ctx.pages.base.check_an_element_is_present(DocumentPageLocators.CANCEL_IS_OKAY, timeout=30)

@Then('Статус документа Аннулирован')
def check_cancel_is_okay(ctx: Context):
    ctx.pages.base.check_an_element_is_present(DocumentPageLocators.DOCUMENT_IS_CANCEL, timeout=30)

@Then('Ссылка в документе Документ аннулирован')
def check_cancel_is_okay(ctx: Context):
    ctx.pages.base.check_an_element_is_present(DocumentPageLocators.DOCUMENT_IS_CANCEL_IN_DOCUMENT, timeout=30)

@When('Кликаем по документу в статусе Требуется аннулирование')
def click_at_document_in_status_is_cancel(ctx: Context):
    ctx.pages.base.click(DocumentPageLocators.DOCUMENT_IN_STATUS_CANCEL)

@When('Переходим в реестр Предложение об аннулировании')
def click_at_document_in_status_is_cancel(ctx: Context):
    ctx.pages.base.click(DocumentPageLocators.REGISTER_OFFER_CANCEL)

@Then('Жмем кнопку Отклонить')
def click_at_reject_cancel(ctx: Context):
    ctx.pages.base.check_an_element_is_present(DocumentPageLocators.BUTTON_REJECT_CANCEL, timeout=90)
    ctx.pages.base.click(DocumentPageLocators.BUTTON_REJECT_CANCEL)

@Then('Ожидаем появления формы {value_text}')
def wait_form_and_input_and_click_accept(ctx: Context, value_text: str):
    ctx.pages.base.check_an_element_is_present(DocumentPageLocators.NOTIFICATION_TEXT, timeout=10)
    name = ctx.pages.base.get_text_from_element(DocumentPageLocators.NOTIFICATION_TEXT)
    assert name == value_text, f'Должно быть "{name}", ожидалось "{value_text}"'


@Then('Вводим причину {value} и жмем Подтвердить')
def write_text_and_click_button(ctx: Context, value: str):
    ctx.pages.document.input_text_in_field_cancel(value)
    ctx.pages.base.click(DocumentPageLocators.BUTTON_ACCEPT_NOTIFICATION_TEXT)

@Then('Ожидаем всплывающее сообщения и жмем кнопку подробнее')
def wait_message_and_click_button_more(ctx: Context):
    ctx.pages.base.check_an_element_is_present(DocumentPageLocators.MESSAGE_ABOUT_CANCEL, timeout=30)
    ctx.pages.base.click(DocumentPageLocators.MESSAGE_ABOUT_CANCEL)

@Then('Проверяем текст {value}')
def check_text_value(ctx: Context, value: str):
    name = ctx.pages.base.get_text_from_element(DocumentPageLocators.TEXT_AFTER_REFUSE_CANCEL)
    assert name == value, f'Должно быть "{name}", ожидалось "{value}"'

@Then('Переходим в реестр Уведомление об уточнении')
def open_register_and_check_text(ctx: Context):
    ctx.pages.base.click(DocumentPageLocators.REGISTER_NOTIFICATION)


@Then('Переходим в режим чтения текста и видим текст {value}')
def click_at_button_and_read_text(ctx: Context, value:str):
    ctx.pages.base.click(DocumentPageLocators.BUTTON_FOR_READ_TEXT_AFTER_REFUSE_CANCEL)
    name = ctx.pages.base.get_text_from_element(DocumentPageLocators.FIELD_WITH_TEXT_CANCEL)
    assert name == value, f'Должно быть "{name}", ожидалось "{value}"'

@When('Проверяем наличе кнопки {value} и нажимаем ее')
def check_button_and_click_her(ctx: Context, value: str):
    name = ctx.pages.base.get_text_from_element(DocumentPageLocators.BUTTON_DECLINE)
    assert name == value, f'Должно быть "{name}", ожидалось "{value}"'
    ctx.pages.base.click(DocumentPageLocators.BUTTON_DECLINE)

@Then('Ожидаем форму {value}')
def check_at_open_form(ctx: Context, value: str):
    name = ctx.pages.base.get_text_from_element(DocumentPageLocators.NOTIFICATION_TEXT)
    assert name == value, f'Должно быть "{name}", ожидалось "{value}"'

@Then('Вводим причину отклонения {value} и нажимаем Принять')
def click_at_field_and_write_text(ctx: Context, value: str):
    ctx.pages.base.check_an_element_is_present(DocumentPageLocators.FIELD_ACCEPT_CANCEL, timeout=10)
    ctx.pages.document.input_value_in_field_cancel(value)
    time.sleep(1)
    ctx.pages.base.click(DocumentPageLocators.BUTTON_ACCEPT_CANCEL)
    time.sleep(2)

@Then('Проверяем статус документа {value} и появление реестра {value_notification}')
def check_status_document(ctx: Context, value: str, value_notification: str):
    ctx.pages.base.check_an_element_is_present(DocumentPageLocators.STATUS_DOCUMENT_DECLINE, timeout=30)
    name = ctx.pages.base.get_text_from_element(DocumentPageLocators.STATUS_DOCUMENT_DECLINE)
    assert name == value, f'Должно быть "{name}", ожидалось "{value}"'
    ctx.pages.base.check_an_element_is_present(DocumentPageLocators.REGISTER_NOTIFICATION, timeout=30)
    name = ctx.pages.base.get_text_from_element(DocumentPageLocators.REGISTER_NOTIFICATION)
    assert name == value_notification, f'Должно быть "{name}", ожидалось "{value_notification}"'

@Then('Кликаем по флагу Ответная подпись')
def click_at_flag(ctx: Context):
    ctx.pages.base.click(DocumentPageLocators.FLAG_RESPONSE_SIGNATURE)