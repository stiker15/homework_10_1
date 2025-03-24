from src.utils import read_transactions
from src.external_api import convert_to_rub


file_path = "data/operations.json"
transactions = read_transactions(file_path)

for transaction in transactions:
    amount_info = transaction.get('operationAmount', {})
    amount = amount_info.get('amount', 0)
    currency_code = amount_info.get('currency', {}).get('code')

    transaction_data = {
        'amount': amount,
        'currency': currency_code
    }

    converted_amount = convert_to_rub(transaction_data)
    print(f"Конвертированная сумма: {converted_amount} RUB")
