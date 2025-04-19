import re
from collections import Counter


def filter_transactions_by_description(transactions, search_string):
    """
       Фильтрует список транзакций, оставляя только те, в описании которых содержится заданная строка.

       Args:
           transactions (list of dict): Список транзакций, где каждая транзакция представлена словарем, содержащим как
           минимум ключ 'description'.
           search_string (str): Строка для поиска в описаниях транзакций.

       Returns:
           list of dict: Список транзакций, описание которых содержит строку поиска, без учета регистра.
       """
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    return [transaction for transaction in transactions if pattern.search(transaction.get('description', ''))]


def count_transactions_by_category(transactions, categories):
    """
        Подсчитывает количество транзакций в каждой из указанных категорий, где категория должна быть точно равна
        описанию транзакции.

        Args:
            transactions (list of dict): Список транзакций, где каждая транзакция представлена словарем с ключом
            'description'.categories (list of str): Список категорий, которые нужно искать в описаниях транзакций.

        Returns:
            dict: Словарь, где ключи — это категории (точные строки в описаниях транзакций), а значения —
            количество транзакций в каждой категории.
        """
    transactions_discription = [
        transaction.get('description') for transaction in transactions if transaction.get('description') in categories]
    return dict(Counter(transactions_discription))
