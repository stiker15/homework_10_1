import os

import requests
from dotenv import load_dotenv

load_dotenv()


def convert_to_rub(transaction):
    """Конвертирует сумму транзакции в рубли."""
    amount = transaction.get('amount')
    currency = transaction.get('currency')

    if currency in ['USD', 'EUR']:
        api_key = os.getenv('API_KEY')
        response = requests.get(
            f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}",
            headers={"apikey": api_key}
        )
        if response.status_code == 200:
            return float(response.json().get('result', amount))
    return float(amount)
