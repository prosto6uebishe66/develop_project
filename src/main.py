from utills import format_from_account
from utills import format_to_account
from utills import date_show
from utills import get_sort_transaction


def five_transactions(json_path):
    five_transaction = []
    transactions = get_sort_transaction(json_path)
    # Получаем последние 5 транзакций
    five_transaction = transactions[-5:] if len(transactions) >= 5 else transactions
    return five_transaction

def get_transaction(json_path):
    info_str = ''
    for ex in five_transactions(json_path):
        info_str_1 = (f'{date_show(ex.get("date"))} '
                      f'{ex.get("description")}\n')

        if format_from_account(ex.get("from")) is None:
            info_str_2 = f'{format_from_account(ex.get("from"))} '
        else:
            info_str_2 = (
                f'{format_from_account(ex.get("from"))} '
                f'{format_from_account(ex.get("to"))}\n')

        info_str_3 = (f'{ex.get("operationAmount", {}).get("amount", "0")}'
                      f'{ex.get("operationAmount", {}).get("currency", {}).get("name", "")}\n')

        info_str += info_str_1
        info_str += info_str_2
        info_str += info_str_3 + '\n'

    return info_str

print(get_transaction('operation.json'))