from tests.input_data import transactions



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


def transaction_descriptions(transactions):
    for transaction in transactions:
        yield transaction.get("description", "Описание не найдено")

descriptions = transaction_descriptions(transactions)
for i in range(5):
    print(next(descriptions))


def card_number_generator(start, stop):
    for number in range(start, stop + 1):
        # Форматируем номер карты с ведущими нулями и пробелами
        card_number = f"{number:016}"
        formatted_card_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield formatted_card_number

# Пример использования функции
for card_number in card_number_generator(1, 7):
    print(card_number)