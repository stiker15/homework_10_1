from unittest import TestCase, mock

from src.external_api import convert_to_rub


class TestExternalAPI(TestCase):
    @mock.patch('src.external_api.requests.get')
    def test_convert_to_rub_usd(self, mock_get):
        mock_response = mock.Mock()
        mock_response.json.return_value = {'result': 7500}
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        transaction = {'amount': 100, 'currency': 'USD'}
        result = convert_to_rub(transaction)
        self.assertEqual(result, 7500.0)

    @mock.patch('src.external_api.requests.get')
    def test_convert_to_rub_eur(self, mock_get):
        mock_response = mock.Mock()
        mock_response.json.return_value = {'result': 8900}
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        transaction = {'amount': 100, 'currency': 'EUR'}
        result = convert_to_rub(transaction)
        self.assertEqual(result, 8900.0)

    def test_convert_to_rub_without_conversion(self):
        transaction = {'amount': 100, 'currency': 'RUB'}
        result = convert_to_rub(transaction)
        self.assertEqual(result, 100.0)
