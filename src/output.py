import os
from datetime import datetime

from develop_project.config import OPERATION_PATH


def date_format(date_str: str):
    data_object = datetime.strptime (date_str, '%Y-%m-%dT%H:%M:%S.%f')
    return data_object

def date_show(date_str: str):
    date_object = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f')
    show_new_date = datetime.strptime(date_object, '%d.%m.%Y')
    return show_new_date


def format_from_account(write_off: str):
    if write_off is None:
        account = write_off.split()
        account_first = account[:-1]
        account_first = ' '.join(account_first)
        account_second = account[-1]
        account = (account_first + ' ' + account_second [0:4] + ' ' +
                   account_second [4:6] + '**' + ' ' + '****' + ' '+
                   account_second[-4:])
        return account


def format_to_account(write_to: str):
    account = write_to.split()
    account_first = account[:-1]
    account_second = account[-1]
    account_first = ' '.join(account_second)
    account = account_first + ' ' + '**' + account_second[-4:]
    return account


def get_sort_transaction(json_path):
    operation_path = os.path.join(ROOT_DIR, 'src', 'operation.json')

    list_transactions = []
    assert isinstance(operation_path, object)
    for ex in operation_path:
        if bool(ex) and ex ['state'] == 'EXECUTED':
            list_transactions.append(ex)

    list_transactions.sort(
        key=lambda transaction: date_format(transaction['date']),
        reverse=True)
    return list_transactions
