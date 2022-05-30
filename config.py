import os

# Путь до папки с проектом
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# Путь до папки с файлами для импорта
REPORTS_FOR_IMPORT_PATH = os.path.join(BASE_PATH, "test_data", "files", "reports")

# Путь до папки со скриншотами
SCREENSHOTS_PATH = os.path.join(BASE_PATH, "temp", "screenshots")

# Вспомогательный словарь для хранения тест данных при использовании нескольких окружений.
SETTINGS = {
    "work1": {
        "baseUrl": "https://edo-1.cloud.astral-dev.ru/",
        "mail": "astraledotest@mail.ru",
        "password": "MakI123456",
        "ID_1": "2AEB38AC744-9BDE-4337-A920-3D56E2F456F5",
        "ID_2": "2AEF0AA2E31-3D84-4F87-ACD7-2001E810085E",
        "INCOMING": "/f0aa2e31-3d84-4f87-acd7-2001e810085e/documents/incoming",
        "OUTGOING": "/b38ac744-9bde-4337-a920-3d56e2f456f5/documents/outgoing",
        "DRAFT": "/b38ac744-9bde-4337-a920-3d56e2f456f5/drafts",
    },
    "work2": {
        "baseUrl": "https://edo-2.cloud.astral-dev.ru/",
        "mail": "astraledotest@mail.ru",
        "password": "MakI123456",
        "ID_1": "2AEDCBF5864-B9CB-4EC7-801D-0E7A831B6BC2",
        "ID_2": "2AE8BE142A1-5B65-4FD8-B56A-E6AD69D7D1AE",
        "INCOMING": "/8be142a1-5b65-4fd8-b56a-e6ad69d7d1ae/documents/incoming",
        "OUTGOING": "/dcbf5864-b9cb-4ec7-801d-0e7a831b6bc2/documents/outgoing",
        "DRAFT": "/dcbf5864-b9cb-4ec7-801d-0e7a831b6bc2/drafts",
    },
    "work3": {
        "baseUrl": "https://edo-3.cloud.astral-dev.ru/",
        "mail": "astraledotest@mail.ru",
        "password": "MakI123456",
        "ID_1": "2AE794D3B1F-3E69-4295-91FB-1431130E73B7",
        "ID_2": "2AE6A9E4BED-18B7-45E9-916A-E6D6DEA36E37",
        "INCOMING": "/6a9e4bed-18b7-45e9-916a-e6d6dea36e37/documents/incoming",
        "OUTGOING": "/794d3b1f-3e69-4295-91fb-1431130e73b7/documents/outgoing",
        "DRAFT": "/794d3b1f-3e69-4295-91fb-1431130e73b7/drafts",
    },
    "staging": {
        "baseUrl": "https://edo.astral-dev.ru/",
        "mail": "astraledotest@mail.ru",
        "password": "MakI123456",
        "ID_1": "2AE0432AF92-345F-491F-8C41-F595D76460E0",
        "ID_2": "2AEAC7B0CAB-03B6-4DBA-908F-621B98A18BF3",
        "INCOMING": "/ac7b0cab-03b6-4dba-908f-621b98a18bf3/documents/incoming",
        "OUTGOING": "/0432af92-345f-491f-8c41-f595d76460e0/documents/outgoing",
        "DRAFT": "/0432af92-345f-491f-8c41-f595d76460e0/drafts",
    },
    "prod": {
        "baseUrl": "https://doc.astral.ru/",
        "mail": "astraledotest@mail.ru",
        "password": "MakI123456",
        "ID_1": "2AEB773495D-B814-43C7-9265-0FBABD086A0D",
        "ID_2": "2AE7645029E-C07A-4738-B927-EA1C4E894EFA",
        "INCOMING": "/7645029e-c07a-4738-b927-ea1c4e894efa/documents/incoming",
        "OUTGOING": "/b773495d-b814-43c7-9265-0fbabd086a0d/documents/outgoing",
        "DRAFT": "/b773495d-b814-43c7-9265-0fbabd086a0d/drafts",
    },
}

# Если окружение не указано, по умолчанию откроется прод
STAND = os.environ.get('STAND', 'work2')
CONFIG = SETTINGS[STAND]

# Создаем директорию для хранения скриншотов
if not os.path.exists(SCREENSHOTS_PATH):
    os.makedirs(SCREENSHOTS_PATH)
