import pytest

from src.widget import get_date, mask_account_card

#Тестирование вывода замаскированных номеров с разными названиями карт
def test_mask_card():

    assert mask_account_card("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"

    assert mask_account_card("MasterCard 7158300734726758") == "MasterCard 7158 30** **** 6758"

    assert mask_account_card("Visa Classic 6831982476737658") == "Visa Classic 6831 98** **** 7658"

    assert mask_account_card("Visa Gold 5999414228426353") == "Visa Gold 5999 41** **** 6353"

# Тестирование вывода замаскированного счета
def test_mask_account():

    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"

# Тестирование правильности преобразования даты
@pytest.mark.parametrize("input_date, expected_output", [
    ("2023-10-01T15:30:00", "01.10.2023"),
    ("2020-01-15T12:00:00", "15.01.2020"),
    ("1999-12-31T23:59:59", "31.12.1999"),
    ("2000-02-29T00:00:00", "29.02.2000"),
    ("2023-11-15T08:45:00", "15.11.2023"),
])
def test_get_date(input_date, expected_output):
    assert get_date(input_date) == expected_output
