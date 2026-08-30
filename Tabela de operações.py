n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
o = 0
print('''            [ 1 ] SOMAR
            [ 2 ] MULTIPLICAR
            [ 3 ] MAIOR
            [ 4 ] DIVIDIR
            [ 5 ] Novos valores
            [ 6 ] SAIR DO PROGRAMA''')
while o != 6:
    o = int(input('>>>>> Qual é a sua opção: '))
    if o == 1:
        s = n1 + n2
        print(f'A soma entre {n1} e {n2} é {s}')
    elif o == 2:
        M = n1 * n2
        print('A mutiplicação entre {} e {} é {}'.format(n1, n2, M))
    elif o == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior número entre {} e {} é {}'.format(n1, n2, maior))
    elif o == 4:
        Di = n1 / n2
        print('A divisão entre {} e {} é {:.2f}'.format(n1, n2, Di))
    elif o == 5:
        print('informe os valores novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif o == 6:
        print('Finalizando...')
    else:
        print('Opção invalida! Tente novamente.')
print('Fim do programa! Volte sempre!')