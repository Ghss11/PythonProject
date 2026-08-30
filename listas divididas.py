lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    while True:
        o = input('Deseja continuar? [S/N]').strip().upper()
        if o in 'S' or o in 'SIM':
            break
        elif o in 'N' or o in 'NÃO':
            print(f'A lista completa é {lista}')
            pares = [n for n in lista if n % 2 == 0]
            impares = [n for n in lista if n % 2 != 0]
            print(f'Os valores pares: {pares}')
            print(f'Os valores impares: {impares}')
            exit()
        else:
            print('Opção inválida, tente novamente!')



