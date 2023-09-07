
def mask_card_number(card_number):
    name_card, digits = card_number.split(' ')
    if name_card != ' ':
        return f'{name_card} {digits[:4]} {digits[:2]}** **** {digits[-4:]}'
    else:
        return f'{digits[:4]} {digits[:2]}** **** {digits[-4:]}'