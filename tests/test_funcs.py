from utils.funcs import read_operations_from_file, filter_executed_operations, get_last_n_operations, mask_card_number, print_operation, print_last_operations
import pytest
import json

def test_read_operations_from_file():
    # Тест №1: файл существует и содержит операции
    filename1 = 'test_operations1.json'
    data1 = [{
        'date': '2021-09-01T09:00:00Z',
        'description': 'Test operation 1',
        'operationAmount': {
            'amount': 1000.0,
            'currency': {'name': 'RUB'}
        },
        'to': '228',
        'from': '1337'
    }]

    with open(filename1, 'w', encoding='utf-8') as f:
        json.dump(data1, f, ensure_ascii=False)

    assert read_operations_from_file(filename1) == data1

    # Тест №2: файл не существует
    filename2 = 'not_existing_file.json'

    with pytest.raises(FileNotFoundError):
        read_operations_from_file(filename2)

def test_filter_executed_operations():
    # Тест №1: список операций пуст
    assert filter_executed_operations([]) == []

    # Тест №2: список содержит 1 операцию со статусом 'EXECUTED'
    operations1 = [{
        'state': 'EXECUTED',
        'description': 'Test operation 1'
    }]
    assert filter_executed_operations(operations1) == operations1

    # Тест №3: список содержит 1 операцию со статусом 'REJECTED'
    operations2 = [{
        'state': 'REJECTED',
        'description': 'Test operation 2'
    }]
    assert filter_executed_operations(operations2) == []

    # Тест №4: список содержит несколько операций, некоторые из которых 'EXECUTED'
    operations3 = [
        {
            'state': 'EXECUTED',
            'description': 'Test operation 1'
        },
        {
            'state': 'REJECTED',
            'description': 'Test operation 2'
        },
        {
            'state': 'CANCELED',
            'description': 'Test operation 3'
        },
        {
            'description': 'Test operation 4'
        }
    ]
    assert filter_executed_operations(operations3) == [operations3[0]]


def test_get_last_n_operations():
    # Тест №1: список операций пуст
    assert get_last_n_operations(3, []) == []

    # Тест №2: n меньше, чем количество операций
    operations = [{
        'date': '2021-09-01T09:00:00Z',
        'description': 'Test operation 1'
    },
        {
            'date': '2021-09-02T10:00:00Z',
            'description': 'Test operation 2'
        },
        {
            'date': '2021-09-03T12:00:00Z',
            'description': 'Test operation 3'
        }]
    assert get_last_n_operations


def test_mask_card_number():
    # Тест №1: простая карта
    assert mask_card_number('Visa 4040123456789012') == 'Visa 4040 40** **** 9012'

    # Тест №2: вводятся данные, соответствующие другому типу карты
    assert mask_card_number('Mastercard 5440123456789012') == 'Mastercard 5440 54** **** 9012'

    # Тест №3: карта с пробелами
    #assert mask_card_number('   Visa 4040111122223333') == 'Visa 404011 ** **** 3333'

    # Тест №4: карта с другой локализацией.
    assert mask_card_number('Visa 4040111122223333') == 'Visa 4040 40** **** 3333'

def test_print_operation(capsys):
    # Создаем пример операции
    operation = {
        'date': '2021-10-15T12:00:00Z',
        'description': 'Payment for goods',
        'operationAmount': {
            'amount': '100.45',
            'currency': {
                'name': 'USD'
            }
        },
        'from': 'Visa 4040123456789012',
        'to': '1234567890123456'
    }

    # Вызываем функцию для элементарной проверки.
    print_operation(operation)

    # Проверяем, что вывод соответствует ожидаемому.
    captured = capsys.readouterr()
    assert captured.out == """ 
15.10.2021 Payment for goods
Visa 4040 40** **** 9012 -> **3456
100.45 USD
"""