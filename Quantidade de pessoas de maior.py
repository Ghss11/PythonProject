from datetime import date
tM = 0
tm = 0
for c in range(1, 8):
    n = int(input('Em qual ano nasceu a {}ª pessoa? '.format(c) ))

    atual = date.today().year
    i = atual - n

    if i >= 18:
        print('A {}ª pessoa é de maior \n'.format(c))
        tM += 1
    else:
        print('A {}ª pessoa é de menor\n '.format(c))
        tm += 1
print('Temos {} pessoas de maior'.format(tM))
print('Temos {} pessoas de menor'.format(tm))