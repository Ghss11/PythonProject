maior = 0
menor = 0
for c in range(1, 6):
    salário = float(input('Qual é o salario do {}ª funcionário: R$'.format(c)))
    if c == 1:
        maior = salário
    if salário > maior:
        maior = salário
print('O maior salário é R${}'.format(maior))