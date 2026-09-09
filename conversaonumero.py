n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
o = int(input('Sua opção: '))
if o == 1:
    print('O número {} em Binário é {}'.format(n, bin(n)[2:]))

elif o == 2:
    print('O número {} em Octal é {}'.format(n, oct(n)[2:]))

else:
    print('O número {}  em Hexadecimal é {}'.format(n, hex(n)[2:]))