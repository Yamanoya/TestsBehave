import os

# Путь до папки с проектом
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# Путь до папки с файлами для импорта
REPORTS_FOR_IMPORT_PATH = os.path.join(BASE_PATH, "test_data", "files", "reports")

# Путь до папки со скриншотами
SCREENSHOTS_PATH = os.path.join(BASE_PATH, "temp", "screenshots")

# Вспомогательный словарь для хранения тест данных при использовании нескольких окружений.
SETTINGS = {
    "prod": {
        "baseUrl": "https://edo-2.cloud.astral-dev.ru/",
        "mail": "astraledotest@mail.ru",
        "password": "MakI123456",
    }
}

# Если окружение не указано, по умолчанию откроется прод
STAND = os.environ.get('STAND', 'prod')
CONFIG = SETTINGS[STAND]

# Создаем директорию для хранения скриншотов
if not os.path.exists(SCREENSHOTS_PATH):
    os.makedirs(SCREENSHOTS_PATH)
