import json
from datetime import datetime


def print_last_operations(n=5):
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
    print()


def mask_card_number(card_number):
    name_card, digits = card_number.split(' ')
    if name_card != ' ':
        return f'{name_card} {digits[:4]} {digits[:2]}** **** {digits[-4:]}'
    else:
        return f'{digits[:4]} {digits[:2]}** **** {digits[-4:]}'


print_last_operations()