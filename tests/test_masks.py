from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(not_16_digits):
    # Тестирование с корректным номером
    assert get_mask_card_number("1234567891234567") == "1234 56** **** 4567"
    # Тестирование слишком большого номера
    assert get_mask_card_number("123456789123456789") == not_16_digits
    # Тестирование слишком маленького номера
    assert get_mask_card_number("123456789") == not_16_digits
    # Тестирование содержания только цифр в номере
    assert get_mask_card_number("1234567812345678g") == not_16_digits


def test_get_mask_account(not_20_digits):
    # Тестирование с корректным номером
    assert get_mask_account("12345678912345678910") == "**8910"
    # Тестирование слишком большого номера
    assert get_mask_account("123456789123456789123") == not_20_digits
    # Тестирование слишком маленького номера
    assert get_mask_account("123456789") == not_20_digits
    # Тестирование содержания только цифр в номере
    assert get_mask_account("1234567891234567891g") == not_20_digits
