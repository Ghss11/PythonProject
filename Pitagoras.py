from math import sqrt, trunc
n1 = float(input('Qual é o valor do cateto oposto:'))
n2 = float(input('Qual é o valor do cateto adjacente:'))
n3 = sqrt(n1**2 + n2**2)
print('A hipotenusa vai medir:{}'.format(trunc(n3)))