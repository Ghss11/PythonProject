lista = []
while True:
    lista.append(input('Digite um valor: '))
    while True:
        o = str(input('Quer continuar? [S/N] ')).upper()
        if o in 'S' or o == 'SIM' :
            break
        elif o in 'N' or o == 'NÃO' or o == 'NAO':
            print(sorted(set(lista)))
            exit()
        else:
            print('Opção inválida, tente novamente!')


