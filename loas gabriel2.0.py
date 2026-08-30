print('\033[33m==\033[m' * 10,'\033[7;30;47mLOJAS GABRIEL\033[m', '\033[33m==\033[m' * 10)
menor = maior = s = cont = 0
barato = ''
while  True:
    n = str(input('Nome do produto: '))
    p = float(input('Preço: R$  '))
    Q = ' '
    s += p
    cont += 1
    if cont == 1:
        menor = p
        barato = n
    else:
        if p < menor:
            menor = p
            barato = n

    while Q not in 'SN':
        Q = str(input('Quer continuar? (S/N)')).strip().upper()[0]
    if Q == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R$ {s}')
print(f'O produto mais barato foi o {barato} e custou R${menor}.')




