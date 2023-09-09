from utils.funcs import read_operations_from_file, filter_executed_operations, get_last_n_operations, mask_card_number, print_operation, print_last_operations

def test_read_operations_from_file():
    ...


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