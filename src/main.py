from develop_project.config import OPERATION_PATH
from develop_project.src.utills import format_from_account
from develop_project.src.utills import date_show
from develop_project.src.utills import get_sort_transaction


def five_transactions(json_path):
    transactions = get_sort_transaction(json_path)
    # Получаем последние 5 транзакций
    five_transaction = transactions[:5] if len(transactions) >= 5 else transactions
    return five_transaction

def get_transaction(json_path):
    info_str = ''
    for ex in five_transactions(json_path):
        # Форматируем дату и описание
        date_str = date_show(ex.get("date", "")) or ""
        description_str = ex.get("description", "")

        info_str_1 = f'{date_str} {description_str}\n'

        # Форматируем поля "from" и "to"
        from_account_str = format_from_account(ex.get("from"))
        to_account_str = format_from_account(ex.get("to"))

        if from_account_str is None:
            from_account_str = ""
        if to_account_str is None:
            to_account_str = ""

        info_str_2 = f'{from_account_str} -> {to_account_str}\n'

        # Форматируем сумму и валюту
        operation_amount = ex.get("operationAmount", {})
        amount_str = operation_amount.get("amount", "0")
        currency_str = operation_amount.get("currency", {}).get("name", "")

        info_str_3 = f'{amount_str} {currency_str}\n'

        # Объединяем все строки
        info_str += info_str_1
        info_str += info_str_2
        info_str += info_str_3 + '\n'

    return info_str


if __name__=="__main__":
    print(get_transaction(OPERATION_PATH))
