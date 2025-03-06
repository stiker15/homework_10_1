import pytest

from src.processing import filter_by_state, sort_by_date


# Тестируем фильтрацию по состоянию 'EXECUTED'
@pytest.mark.parametrize("state, expected", [
    ("EXECUTED", [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ])
])
def test_filter_by_state(transaction, state, expected):
    filtered = filter_by_state(transaction, state)
    assert sorted(filtered, key=lambda x: x['id']) == sorted(expected, key=lambda x: x['id'])


    # Тестируем сортировку по дате в порядке убывания
def test_sort_by_date_descending(sample_data):
    sorted_data = sort_by_date(sample_data)
    expected_data = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    ]
    assert sorted_data == expected_data


def test_sort_by_date_ascending(sample_data):
    # Поменяем порядок сортировки на восходящий для этого теста
    sorted_data = sort_by_date(sample_data)[::-1]
    expected_data = sorted(sample_data, key=lambda x: x['date'])
    assert sorted_data == expected_data


def test_sort_by_identical_dates():
    # Порядок должен оставаться прежним для одинаковых дат
    identical_dates = [
        {'id': 1, 'state': 'EXECUTED', 'date': '2023-10-01T15:30:00.000000'},
        {'id': 2, 'state': 'EXECUTED', 'date': '2023-10-01T15:30:00.000000'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2023-10-01T15:30:00.000000'},
    ]

    sorted_data = sort_by_date(identical_dates)
    assert sorted_data == identical_dates


def test_sort_by_date_invalid_format():
    # Тесты на работу функции с некорректными или нестандартными форматами дат
    invalid_data = [
        {'id': 1, 'state': 'EXECUTED', 'date': 'Invalid Date'},
        {'id': 2, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    ]

    with pytest.raises(ValueError):
        sort_by_date(invalid_data)


def test_sort_by_date_nonstandard_format():
    nonstandard_data = [
        {'id': 1, 'state': 'EXECUTED', 'date': '2023/10/01 15:30:00'},
        {'id': 2, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    ]

    with pytest.raises(ValueError):
        sort_by_date(nonstandard_data)


# Проверка на подачу пустого списка
def test_sort_empty_list():
    assert sort_by_date([]) == []
