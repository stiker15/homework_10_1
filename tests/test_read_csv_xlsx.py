import unittest
from unittest.mock import patch
import pandas as pd
from src.read_CSV_XLSX import read_csv_file, read_financial_transactions_from_excel


class TestReadCSVFile(unittest.TestCase):
    """
    Тестовый класс для функции read_csv_file.
    Проверяет, что функция корректно читает данные из CSV-файла
    и возвращает их в виде списка словарей.
    """

    @patch('src.read_CSV_XLSX.pd.read_csv')
    def test_read_csv_file(self, mock_read_csv):
        """
        Тестирует read_csv_file на корректность преобразования
        данных из CSV-файла в список словарей.
        Использует mock для замены фактического чтения CSV.
        """
        mock_data = pd.DataFrame({
            'Date': ['2023-01-01', '2023-01-02'],
            'Amount': [150, 250],
            'Description': ['Transaction 1', 'Transaction 2']
        })

        mock_read_csv.return_value = mock_data
        csv_path = 'transactions.csv'

        expected_transactions = [
            {'Date': '2023-01-01', 'Amount': 150, 'Description': 'Transaction 1'},
            {'Date': '2023-01-02', 'Amount': 250, 'Description': 'Transaction 2'}
        ]
        data_transactions = read_csv_file(csv_path)

        self.assertEqual(data_transactions, expected_transactions)

        mock_read_csv.assert_called_once_with(csv_path)


class TestReadFinancialTransactionsFromExcel(unittest.TestCase):
    """
    Тестовый класс для функции read_financial_transactions_from_excel.
    Проверяет, что функция корректно читает данные из Excel-файла
    и возвращает их в виде списка словарей.
    """

    @patch('src.read_CSV_XLSX.pd.read_excel')
    def test_read_financial_transactions_from_excel(self, mock_read_excel):
        """
        Тестирует read_financial_transactions_from_excel на корректность
        преобразования данных из Excel-файла в список словарей.
        Использует mock для замены фактического чтения Excel.
        """
        test_data = {
            'Date': ['2023-10-01', '2023-10-02'],
            'Amount': [100.0, 200.0]
        }
        mock_df = pd.DataFrame(test_data)
        mock_read_excel.return_value = mock_df

        data_transactions = read_financial_transactions_from_excel('fake_path.xlsx')

        expected_transactions = [
            {'Date': '2023-10-01', 'Amount': 100.0},
            {'Date': '2023-10-02', 'Amount': 200.0}
        ]

        # Проверка, что результат соответствует ожиданиям
        self.assertEqual(data_transactions, expected_transactions)
        # Проверка, что pd.read_excel был вызван с корректным аргументом
        mock_read_excel.assert_called_once_with('fake_path.xlsx')


if __name__ == '__main__':
    unittest.main()
