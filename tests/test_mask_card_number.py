from utils.mask_card_number import mask_card_number

def test_mask_card_number():
    assert mask_card_number('Счет 46363668439560358409') == 'Счет 4636 46** **** 8409'
    assert mask_card_number('Maestro 6000111122223333') == 'Maestro 6000 60** **** 3333'
    assert mask_card_number(' 4276380012345678') == ' 4276 42** **** 5678'
