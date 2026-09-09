n = str(input('Digite uma frase: ')).replace(' ', '').upper()
n_invertido = n[::-1]
print('A frase {} invertida fica {}'.format(n, n_invertido))
if n == n_invertido:
    print('Temos um palíndromo')
else:
    print('a frase digitada não é um palíndromo')