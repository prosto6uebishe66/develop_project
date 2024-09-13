from src import output


def five_transactions(json_path):
    five_transaction = []
    for ex in range(5):
        five_transaction.append(src.output.get_sort_transaction(json_path)[ex])
    return five_transaction


def get_transaction(json_path):
    info_str = ''
    for ex in five_transactions(json_path):
        info_str_1 = (f'{src.output.date_show(ex.get("date"))}'
                      f'{ex.get("description")}\n')

        if src.functions.format_from_account(ex.get('from')) is None:
            info_str_2 = f'{src.functions.format_from_account(ex.get("from"))} '
        else:
            info_str_2 = (
                f'{src.functions.format_from_account(ex.get("from"))}'
                f'{src.functions.format_from_account(ex.get("to"))}\n')  # Исправленный вызов

        info_str_3 = (f'{ex.get("operationAmout").get("amout")}'
                      f'{ex.get("operationAmout").get("currency").get("name")}\n')

        info_str += info_str_1
        info_str += info_str_2
        info_str += info_str_3 + '\n'

    return info_str


print(get_transaction('operation.json'))
