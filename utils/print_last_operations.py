import json
from datetime import datetime
from utils.mask_card_number import mask_card_number


def print_last_operations(n=5):
    '''
    Функция принимает на вход JSON файл, читает его и выводит 5 последних операций
    по карте в формате

    <дата перевода> <описание перевода>
    <откуда> -> <куда>
    <сумма перевода> <валюта>

    :param n:
    :return:
    '''
    with open('operations.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

        executed_operations = []

        for op in data:
            if 'state' in op and op['state'] == 'EXECUTED':
                executed_operations.append(op)

    last_operations = [op for op in reversed(data) if 'state' in op and op['state'] == 'EXECUTED'][:n]

    for item in last_operations:
        date_str = item['date']
        date = datetime.fromisoformat(date_str[:-1]) # преобразование строки в объект datetime
        operation = item['description']
        amount = float(item['operationAmount']['amount'])
        currency = str(item['operationAmount']['currency']['name'])
        account_from = item.get('from')
        account_to = item['to']

        print(' ')
        print(f"{date.strftime('%d.%m.%Y')} {operation}")
        if account_from:
            card_from = mask_card_number(account_from)
            print(f"{card_from} -> **{account_to[-4:]}")
        else:
            print(f"**{account_to[-4:]}")
        print(f"{amount:.2f} {currency}")


