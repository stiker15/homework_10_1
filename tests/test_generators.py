import pytest
from src.generators import filter_by_currency

@pytest.mark.parametrize(
    "transactions, currency_code, expected_length",
    [
        (
            [
                {"operationAmount": {"currency": {"code": "USD"}, "amount": 100}},
                {"operationAmount": {"currency": {"code": "EUR"}, "amount": 200}},
                {"operationAmount": {"currency": {"code": "USD"}, "amount": 300}}
            ],
            "USD",
            2
        ),
        (
            [
                {"operationAmount": {"currency": {"code": "EUR"}, "amount": 200}},
                {"operationAmount": {"currency": {"code": "GBP"}, "amount": 150}}
            ],
            "USD",
            0
        ),
        (
            [],
            "USD",
            0
        ),
        (
            [
                {"operationAmount": {"currency": {"code": "EUR"}, "amount": 200}}
            ],
            "USD",
            0
        )
    ]
)
def test_filter_by_currency(transactions, currency_code, expected_length):
    filtered = list(filter_by_currency(transactions, currency_code))
    assert len(filtered) == expected_length