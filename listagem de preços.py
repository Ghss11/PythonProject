listagem = ('Short', 35.00,
            'croped', 30.00,
            'macacão', 60.00,
            'calça', 65.00,
            'bermuda', 40.00,
            'jaqueta', 50.00,
            'saia', 35.00,
            'vestido', 50.00)
print('-' * 40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('-' * 40)
for intem in range(0, len(listagem)):
    if intem % 2 == 0:
        print(f'\033[37m{listagem[intem]:.<30}\033[m', end = '')
    else:
        print(f'\033[32mR${listagem[intem]:>7}\033[m')
print('-' * 40)
