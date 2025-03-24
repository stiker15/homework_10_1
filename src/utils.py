import os
import json


def read_transactions(file_path):
    """
    Читает JSON-файл и возвращает список транзакций.
    Перед каждой операцией в функции добавил print(" "), что бы понимать что работает не верно: p.s. помогло;)
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            print("Файл открыт.")
            data = json.load(file)
            print("Данные загружены.")
            print("Тип данных:", type(data))
            if isinstance(data, list):
                return data
    except FileNotFoundError:
        print("Файл не найден.")
    except json.JSONDecodeError:
        print("Ошибка декодирования JSON.")
    return []

# Пример вызова функции
file_path = "../data/operations.json"
transactions = read_transactions(file_path)
print(transactions)
