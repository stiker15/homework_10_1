import unittest
from src.filter import count_transactions_by_category


class TestTransactionFunctions(unittest.TestCase):

    def setUp(self):
        # Инициализация данных для тестов
        self.transactions = [
            {'id': 1, 'description': 'Payment to Client A', 'amount': 1500},
            {'id': 2, 'description': 'Payment to Vendor B', 'amount': 2000},
            {'id': 3, 'description': 'Refund to Client A', 'amount': -500},
            {'id': 4, 'description': 'Fee for Service', 'amount': -100},
            {'id': 5, 'description': 'Refund to Client A', 'amount': -300},
        ]

        self.categories = ['Payment to Client A', 'Refund to Client A', 'Fee for Service']

    def test_count_transactions_by_category(self):
        # Подсчет категорий
        category_counts = count_transactions_by_category(self.transactions, self.categories)

        # Проверка точной оценки количества транзакций для каждой категории
        self.assertEqual(category_counts['Payment to Client A'], 1)
        self.assertEqual(category_counts['Refund to Client A'], 2)
        self.assertEqual(category_counts['Fee for Service'], 1)

        # Проверка, что нет лишних категорий
        self.assertNotIn('Payment to Vendor B', category_counts)

    def test_no_categories_matched(self):
        # Проверка случая, когда ни одна категория не совпала
        other_categories = ['Nonexistent Category']
        category_counts = count_transactions_by_category(self.transactions, other_categories)
        self.assertEqual(category_counts, {})

    def test_empty_transactions(self):
        # Проверка случая с пустым списком транзакций
        empty_transactions = []
        category_counts = count_transactions_by_category(empty_transactions, self.categories)
        self.assertEqual(category_counts, {})

    def test_empty_categories(self):
        # Проверка случая с пустым списком категорий
        empty_categories = []
        category_counts = count_transactions_by_category(self.transactions, empty_categories)
        self.assertEqual(category_counts, {})


if __name__ == '__main__':
    unittest.main()
