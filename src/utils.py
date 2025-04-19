import json
import logging
import os

# Создание директории logs
log_dir = os.path.join(os.path.dirname(__file__), 'logs')
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Настройка логера для модуля utils
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Настройка file_handler для записи логов в файл
file_handler = logging.FileHandler(os.path.join(log_dir, 'utils.log'), encoding='utf-8')
file_handler.setLevel(logging.DEBUG)

# Настройка формата записи логов
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

# Добавление handler в логер
logger.addHandler(file_handler)


def read_transactions(file_path):
    """
    Читает JSON-файл и возвращает список транзакций.
    Перед каждой операцией в функции добавил print(" "), что бы понимать что работает не верно: p.s. помогло;)
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            logger.debug("Файл открыт.")
            data = json.load(file)
            logger.debug("Данные загружены.")
            if isinstance(data, list):
                logger.info("Транзакции успешно считаны.")
                return data
    except FileNotFoundError:
        logger.error("Файл не найден.")
    except json.JSONDecodeError:
        logger.error("Ошибка декодирования JSON.")
    return []

# Пример вызова функции


file_path = "../data/operations.json"
transactions = read_transactions(file_path)
