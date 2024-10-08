import json
import os
from datetime import datetime

from develop_project.config import OPERATION_PATH


def date_format(date_str: str):
    data_object = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f')
    return data_object


def date_show(date_str: str):
    date_object = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f')
    show_new_date = date_object.strftime('%d.%m.%Y')
    return show_new_date


def format_from_account(write_off: str):
    if write_off is None:
        return None  # Возвращаем None, если write_off - None
    if write_off[:4] == 'Счет':
        account = write_off.split()
        account_first = account[:-1]
        account_second = account[-1]
        account_first = ' '.join(account_first)
        account = account_first + ' **' + account_second[-4:]

    else:

        account = write_off.split()
        account_first = account[:-1]
        account_first = ' '.join(account_first)
        account_second = account[-1]
        account = (account_first + ' ' + account_second[0:4] + ' ' +
                   account_second[4:6] + '** ' + '****' + ' ' +
                   account_second[-4:])
    return account


def get_sort_transaction(json_path):
    with open(json_path, 'r') as f:
        operation_data = json.load(f)

    list_transactions = []
    for ex in operation_data:
        if bool(ex) and ex['state'] == 'EXECUTED':
            list_transactions.append(ex)

    list_transactions.sort(
        key=lambda transaction: date_format(transaction['date']),
        reverse=True)
    return list_transactions
