def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты.

    :param card_number: Номер карты (без пробелов)
    :return: Маскированный номер карты формата XXXX XX** **** XXXX
    """
    card_str = str(card_number)
    if len(card_str) != 16 or not card_number.isdigit():
        return "Номер карты должен содержать ровно 16 цифр и состоять только из цифр."

    masked_card = f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"

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
        return "Некорректный номер счета. Должно быть 20 цифр."

    # Возвращаем последние 4 цифры
    return f"**{account_str[-4:]}"
