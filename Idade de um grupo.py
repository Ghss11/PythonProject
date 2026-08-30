s = 0
maioridade = 0
nomevelho = 0
totmulher = 0
tothomem = 4 - totmulher
for c in range(1,5):
    print('----- {}ªPESSOA -----'.format(c))
    n = str(input('NOME: '))
    i = int(input('IDADE: '))
    sexo = str(input('Sexo [M/F]: '))
    s += i
    m = s / c
    if c == 1 and  sexo in 'Mm':
        maioridade = i
        nomevelho = n
    if sexo in 'Mm' and i > maioridade:
        maioridade = i
        nomevelho = n
    if sexo in 'Ff':
        totmulher += 1
print('A média das idades desse grupo é  de {:.1f} anos'.format(m))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridade, nomevelho))
print('Esse grupo tem {} mulheres'.format(totmulher))
print('Esse grupo tem {} homens'.format(totmulher))
