import pytest

from src.generators import (card_number_generator, filter_by_currency,
                            transaction_descriptions)


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


def test_transaction_descriptions(transactions):
    descriptions = list(transaction_descriptions(transactions))
    expected_descriptions = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации"
    ]
    assert descriptions == expected_descriptions


def test_transaction_descriptions_empty():
    descriptions = list(transaction_descriptions([]))
    assert descriptions == []


@pytest.mark.parametrize(
    "start, stop, expected_numbers",
    [
        (1, 1, ["0000 0000 0000 0001"]),
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
        (10, 12, ["0000 0000 0000 0010", "0000 0000 0000 0011", "0000 0000 0000 0012"]),
        (9999999999999990, 9999999999999992, [
            "9999 9999 9999 9990",
            "9999 9999 9999 9991",
            "9999 9999 9999 9992"
        ]),
    ]
)
def test_card_number_generator(start, stop, expected_numbers):
    generated_numbers = list(card_number_generator(start, stop))
    assert generated_numbers == expected_numbers


def test_card_number_generator_empty_range():
    generated_numbers = list(card_number_generator(5, 4))
    assert generated_numbers == []
