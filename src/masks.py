def get_mask_card_number(card_number: int) -> str:
    """
    Маскирует номер банковской карты.

    :param card_number: Номер карты (без пробелов)
    :return: Маскированный номер карты формата XXXX XX** **** XXXX
    """
    card_str = str(card_number)
    if len(card_str) != 16:
        raise ValueError("Номер карты должен содержать ровно 16 цифр.")

    masked_card = f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"

    return masked_card


def get_mask_account(account_number: int) -> str:
    """
    Маскирует номер банковского счета.

    :param account_number: Номер счета
    :return: Маскированный номер счета формата **XXXX
    """
    account_str = str(account_number)
    visible_end = account_str[-4:]
    return f"**{visible_end}"
