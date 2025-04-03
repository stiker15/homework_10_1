import pandas as pd


def read_csv_file(csv_file_path):
    """
    Читает данные из CSV-файла и преобразует их в список словарей.

    :param csv_file_path: Путь к CSV-файлу для чтения.
    :return: Список словарей, где каждый словарь представляет собой строку из CSV-файла.
    """
    transactions_df = pd.read_csv(csv_file_path)
    transactions_list = transactions_df.to_dict(orient='records')
    return transactions_list


def read_financial_transactions_from_excel(excel_file_path):
    """
       Читает данные из Excel-файла и преобразует их в список словарей.

       :param excel_file_path: Путь к Excel-файлу для чтения.
       :return: Список словарей, где каждый словарь представляет собой строку из Excel-файла.
       """
    transactions_df = pd.read_excel(excel_file_path)
    transactions_list = transactions_df.to_dict(orient='records')
    return transactions_list


if __name__ == '__main__':
    csv_path = 'transactions.csv'
    transactions = read_csv_file(csv_path)
    print(transactions)

    excel_path = 'transactions_excel.xlsx'
    transactions_excel = read_financial_transactions_from_excel(excel_path)
    print(transactions_excel)
