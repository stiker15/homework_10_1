import pandas as pd


def read_csv_file(csv_file_path):

    df = pd.read_csv(csv_file_path, delimiter=';')
    transactions_list = df.to_dict(orient="records")
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
    csv_path = '../data/transactions.csv'
    transactions = read_csv_file(csv_path)

    excel_path = '../data/transactions_excel.xlsx'
    transactions_excel = read_financial_transactions_from_excel(excel_path)
