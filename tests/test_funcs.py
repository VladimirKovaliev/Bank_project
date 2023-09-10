from utils.funcs import read_operations_from_file, filter_executed_operations, get_last_n_operations, mask_card_number, print_operation, print_last_operations


def test_filter_executed_operations():
    assert filter_executed_operations([]) == []

    operations1 = [{
        'state': 'EXECUTED',
        'description': 'Test operation 1'
    }]
    assert filter_executed_operations(operations1) == operations1

    operations2 = [{
        'state': 'CANCELED',
        'description': 'Test operation 2'
    }]
    assert filter_executed_operations(operations2) == []

    operations3 = [
        {
            'state': 'EXECUTED',
            'description': 'Test operation 1'
        },
        {
            'state': 'CANCELED',
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
    assert get_last_n_operations(3, []) == []

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
    assert mask_card_number('Visa 4040123456789012') == 'Visa 4040 40** **** 9012'
    assert mask_card_number('Mastercard 5440123456789012') == 'Mastercard 5440 54** **** 9012'
    assert mask_card_number('Visa 4040111122223333') == 'Visa 4040 40** **** 3333'

def test_print_operation(capsys):
    operation = {
        'date': '2021-10-15T12:00:00Z',
        'description': 'Payment',
        'operationAmount': {
            'amount': '100.45',
            'currency': {
                'name': 'USD'
            }
        },
        'from': 'Visa 4040123456789012',
        'to': '1234567890123456'
    }

    print_operation(operation)

    captured = capsys.readouterr()
    assert captured.out == """ 
15.10.2021 Payment
Visa 4040 40** **** 9012 -> **3456
100.45 USD
"""