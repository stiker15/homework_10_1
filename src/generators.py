from tests.input_data import transactions

"""

    Фильтрует список транзакций, возвращая только те, которые соответствуют заданному валютному коду.

    :param transactions (list): Список транзакций, где каждая транзакция представлена в виде словаря,
                             содержащего, среди прочего, информацию о сумме операции в валюте.
    :param currency_code (str): Код валюты (напр. "USD"), по которому необходимо отфильтровать транзакции.
"""


def filter_by_currency(transactions, currency_code):
    for transaction in transactions:
        if (
            transaction.get("operationAmount", {}).get("currency", {}).get("code")
            == currency_code
        ):
            yield transaction


usd_transactions = filter_by_currency(transactions, "USD")
for i in range(2):
    print(next(usd_transactions))

"""
Генерирует описания транзакций из списка транзакций.
    :param transactions (list): Список транзакций, где каждая транзакция представлена в виде словаря,
    который может содержать ключ "description" с текстовой строкой описания.
    Возвращает:
        generator: Генератор, который итерируется по описаниям транзакций.
        Если описание отсутствует, возвращает строку "Описание не найдено".
"""


def transaction_descriptions(transactions):
    for transaction in transactions:
        yield transaction.get("description", "Описание не найдено")


descriptions = transaction_descriptions(transactions)
for i in range(5):
    print(next(descriptions))

"""
Генерирует номера карт в заданном диапазоне, отформатированные с ведущими нулями и пробелами.

    :param start: Начальное число для генерации номеров карт (включительно).
    :param stop: Конечное число для генерации номеров карт (включительно).
    :yield: Форматированный строковый номер карты
"""


def card_number_generator(start, stop):
    for number in range(start, stop + 1):
        # Форматируем номер карты с ведущими нулями и пробелами
        card_number = f"{number:016}"
        formatted_card_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield formatted_card_number


for card_number in card_number_generator(1, 7):
    print(card_number)
