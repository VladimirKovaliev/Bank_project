import json
from datetime import datetime

def read_operations_from_file(filename):
    """Читает json файл и возвращает список операций."""
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data

def filter_executed_operations(operations):
    """Отбирает операции со статусом 'EXECUTED'."""
    return [op for op in operations if 'state' in op and op['state'] == 'EXECUTED']

def get_last_n_operations(n, operations):
    """Возвращает последние n операций."""
    return list(reversed(operations))[:n]

def mask_card_number(card_number):
    '''
    Функция маскирует данные карты, выводя первые 6 и последние 4 цифры
    :param card_number:
    :return:
    '''
    name_card, digits = card_number.split(' ')
    if name_card != ' ':
        return f'{name_card} {digits[:4]} {digits[:2]}** **** {digits[-4:]}'
    else:
        return f'{digits[:4]} {digits[:2]}** **** {digits[-4:]}'

def print_operation(operation):
    """Печатает одну операцию в желаемом формате."""
    date_str = operation['date']
    date = datetime.fromisoformat(date_str[:-1])
    description = operation['description']
    amount = float(operation['operationAmount']['amount'])
    currency = str(operation['operationAmount']['currency']['name'])
    account_from = operation.get('from')
    account_to = operation['to']

    print(' ')
    print(f"{date.strftime('%d.%m.%Y')} {description}")
    if account_from:
        card_from = mask_card_number(account_from)
        print(f"{card_from} -> **{account_to[-4:]}")
    else:
        print(f"{mask_card_number(account_to)}")
    print(f"{amount:.2f} {currency}")

def print_last_operations(n=5, filename='operations.json'):
    '''
    Функция принимает на вход JSON файл, читает его и выводит 5 последних операций
    по карте в формате

    <дата перевода> <описание перевода>
    <откуда> -> <куда>
    <сумма перевода> <валюта>

    :param n:
    :param filename:
    :return:
    '''
    operations = read_operations_from_file(filename)
    executed_operations = filter_executed_operations(operations)
    last_operations = get_last_n_operations(n, executed_operations)
    for operation in last_operations:
        print_operation(operation)