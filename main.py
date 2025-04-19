from src.filter import filter_transactions_by_description
from src.processing import filter_by_state, sort_by_date
from src.utils import read_transactions
from src.read_CSV_XLSX import read_csv_file, read_financial_transactions_from_excel
from src.generators import filter_by_currency, filter_by_currency_csv_xslx
from src.widget import mask_account_card, get_date


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    user_choice = input("Пользователь: ")

    if user_choice == '1':
        file_type = "JSON"
        transactions = read_transactions('data/operations.json')
    elif user_choice == '2':
        file_type = "CSV"
        transactions = read_csv_file('data/transactions.csv')
    elif user_choice == '3':
        file_type = "XLSX"
        transactions = read_financial_transactions_from_excel('data/transactions_excel.xlsx')
    else:
        print("Некорректный выбор, попробуйте снова.")
        return

    print(f"Для обработки выбран {file_type}-файл.")

    # Фильтрация по статусу
    available_statuses = ['EXECUTED', 'CANCELED', 'PENDING']
    status = input(f"Введите статус,{available_statuses} по которому необходимо выполнить фильтрацию:")

    while status.upper() not in available_statuses:
        print(f"Статус операции \"{status}\" недоступен.")
        status = input("Введите статус, по которому необходимо выполнить фильтрацию: EXECUTED, CANCELED, PENDING")
    filtered_transactions = filter_by_state(transactions, status)
    print(f"Операции отфильтрованы по статусу \"{status.upper()}\"")

    # Сортировка по дате
    while True:
        sort_choice = input("Отсортировать операции по дате? Да/Нет: ").strip().lower()
        if sort_choice == 'да':
            order_choice = input("Отсортировать по: 1.Возрастанию, 2.Убыванию? Введите 1 или 2:").strip().lower()
            reverse_order = order_choice == '2'
            filtered_transactions = sort_by_date(filtered_transactions, reverse_order)
            break
        elif sort_choice == 'нет':
            break

    # Фильтрация по валюте
    while True:
        currency_choice = input("Выводить только рублевые транзакции? Да/Нет: ").strip().lower()
        if currency_choice == 'да':
            if file_type == "JSON":
                filtered_transactions = list(filter_by_currency(filtered_transactions, 'RUB'))\

            elif file_type == "CSV" or file_type == "XLSX":
                filtered_transactions = list(filter_by_currency_csv_xslx(filtered_transactions, 'RUB'))
            break
        elif currency_choice == 'нет':
            break
    # Фильтрация по описанию
    desc_filter_choice = input(
        "Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").strip().lower()
    if desc_filter_choice == 'да':
        search_word = input("Введите слово для фильтрации по описанию: ")
        filtered_transactions = filter_transactions_by_description(filtered_transactions, search_word)

    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
        for transaction in filtered_transactions:
            if file_type == "JSON":
                if "перевод" in transaction.get('description', '').lower():
                    print(f"{get_date(transaction.get('date', ''))} {transaction.get('description', '')}")
                    print(f"{mask_account_card(transaction.get('from', ''))} -> "
                          f"{mask_account_card(transaction.get('to', ''))}")
                    print(f"Сумма: {transaction.get('operationAmount', {}).get('amount', 0)} "
                          f"{transaction.get('operationAmount', {}).get('currency', {}).get('name')}\n")
                else:
                    print(f"{get_date(transaction.get('date', ''))} {transaction.get('description', '')}")
                    print(f"{mask_account_card(transaction.get('to', ''))}")
                    print(f"Сумма: {transaction.get('operationAmount', {}).get('amount', 0)} "
                          f"{transaction.get('operationAmount', {}).get('currency', {}).get('name')}\n")
            elif file_type in ["CSV", "XLSX"]:
                if "перевод" in transaction.get('description', '').lower():
                    print(f"{get_date(transaction.get('date', ''))} {transaction.get('description', '')}")
                    print(f"{mask_account_card(transaction.get('from', ''))} -> "
                          f"{mask_account_card(transaction.get('to', ''))}")
                    print(f"Сумма: {transaction.get('amount', 0)} {transaction.get('currency_code')}\n")
                else:
                    print(f"{get_date(transaction.get('date', ''))} {transaction.get('description', '')}")
                    print(f"{mask_account_card(transaction.get('to', ''))}")
                    print(f"Сумма: {transaction.get('amount', 0)} {transaction.get('currency_code')}\n")


if __name__ == "__main__":
    main()
