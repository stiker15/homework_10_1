import unittest
from src.filter import filter_transactions_by_description


class TestTransactionFunctions(unittest.TestCase):

    def setUp(self):
        # Пример данных для тестирования
        self.transactions = [
            {'id': 1, 'description': 'Executed: Payment to Client', 'amount': 1500},
            {'id': 2, 'description': 'Executed: Payment to Vendor', 'amount': 2000},
            {'id': 3, 'description': 'Refund: Client refund', 'amount': -500},
            {'id': 4, 'description': 'Pending: Transfer to Savings', 'amount': 3000},
        ]

        self.categories = ['Payment to Client', 'Refund: Client refund']

    def test_filter_transactions_by_description(self):
        # Тест для поиска по описанию
        filtered = filter_transactions_by_description(self.transactions, 'Executed')
        self.assertEqual(len(filtered), 2)
        self.assertIn(self.transactions[0], filtered)
        self.assertIn(self.transactions[1], filtered)

        # Тест для поиска, не чувствительного к регистру
        filtered_case_insensitive = filter_transactions_by_description(self.transactions, 'client')
        self.assertEqual(len(filtered_case_insensitive), 2)

        # Тест для поиска без результата
        filtered_empty = filter_transactions_by_description(self.transactions, 'NotExistingWord')
        self.assertEqual(len(filtered_empty), 0)
