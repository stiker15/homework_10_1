from typing import Dict, List


def filter_by_state(data_list: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param data_list: Список словарей, содержащих ключ 'state'.
    :param state: Значение для фильтрации по ключу 'state' (по умолчанию 'EXECUTED').
    :return: Новый список словарей с выбранным состоянием.
    """
    result = []  # Создаем новый пустой список для хранения результата

    # Проходим по каждому элементу в data_list
    for item in data_list:
        # Проверяем значение по ключу 'state' в текущем элементе item
        state_value = item.get('state')  # Получаем значение 'state', если оно есть

        # Сравниваем его с ожидаемым значением state
        if state_value == state:
            result.append(item)
    return result


def sort_by_date(data_list, reverse=True):
    return sorted(data_list, key=lambda x: x.get('date'), reverse=reverse)
