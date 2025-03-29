import logging
import os

# Создание директории logs
log_dir = os.path.join(os.path.dirname(__file__), 'logs')
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Настройка логера для модуля masks
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Настройка file_handler для записи логов в файл с указанием кодировки
file_handler = logging.FileHandler(os.path.join(log_dir, 'masks.log'), encoding='utf-8')
file_handler.setLevel(logging.DEBUG)

# Настройка формата записи логов
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

# Добавление handler в логер
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты.

    :param card_number: Номер карты (без пробелов)
    :return: Маскированный номер карты формата XXXX XX** **** XXXX
    """
    card_str = str(card_number)
    if len(card_str) != 16 or not card_number.isdigit():
        logger.error("Номер карты должен содержать ровно 16 цифр и состоять только из цифр.")
        return "Номер карты должен содержать ровно 16 цифр и состоять только из цифр."

    masked_card = f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"
    logger.info("Номер карты замаскирован.")

    return masked_card


def get_mask_account(account_number: str) -> str:
    """
    Возвращает последние 4 цифры банковского счета или сообщение об ошибке, если
    количество цифр в счете некорректно.

    :param account_number: Номер счета
    :return: Последние 4 цифры номера счета или сообщение об ошибке
    """
    account_str = str(account_number)

    # Проверка на достаточное количество цифр
    if len(account_str) != 20 or not account_str.isdigit():
        logging.error("Некорректный номер счета. Должно быть 20 цифр.")
        return "Некорректный номер счета. Должно быть 20 цифр."

    # Возвращаем последние 4 цифры
    logger.info("Маскировка счета выполнена успешно.")
    return f"**{account_str[-4:]}"
