from unittest import TestCase, mock
from src.utils import read_transactions


class TestUtils(TestCase):
    @mock.patch('builtins.open', mock.mock_open(read_data='[]'))
    def test_read_transactions_empty_file(self):
        result = read_transactions("fake_path.json")
        self.assertEqual(result, [])

    @mock.patch('builtins.open', mock.mock_open(read_data='[{"amount": 100}]'))
    def test_read_transactions_valid_data(self):
        result = read_transactions("fake_path.json")
        self.assertEqual(result, [{"amount": 100}])

    @mock.patch('builtins.open', side_effect=FileNotFoundError)
    def test_read_transactions_file_not_found(self, mock_open):
        result = read_transactions("non_existing_path.json")
        self.assertEqual(result, [])
