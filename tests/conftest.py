import pytest


@pytest.fixture
# Фикстура для теста test_get_mask_card_number
def not_16_digits():
    return "Номер карты должен содержать ровно 16 цифр и состоять только из цифр."


@pytest.fixture
#Фикстура для теста test_filter_by_state
def transaction():
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    ]


@pytest.fixture
# Фикстура для теста test_get_mask_account
def not_20_digits():
    return "Некорректный номер счета. Должно быть 20 цифр."


@pytest.fixture
# Фикстура для тестирования функции sort_by_date
def sample_data():
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    ]