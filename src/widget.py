from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info: str) -> str:
    """
    Маскирует номер карты или счета.

    :param info: Строка, содержащая название карты или счета и их номер.
    :return: Строка с замаскированным номером.
    """
    if info.startswith("Счет"):
        return f"{info[:5]}{get_mask_account((info[5:]))}"
    else:
        return f"{info[:-16].strip()} {get_mask_card_number((info[-16:]))}"


def get_date(date_string: str) -> str:
    """
    Преобразует строку с датой в формате 'YYYY-MM-DDTHH:MM:SS'
    в формат 'DD.MM.YYYY'.

    :param date_string: Дата в строковом формате.
    :return: Дата в формате 'DD.MM.YYYY'.
    """
    return date_string[8:10] + '.' + date_string[5:7] + '.' + date_string[:4]
